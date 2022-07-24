import torch
import torch.nn.functional as F

from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig


def classify(config) -> list:
    lines = config.lines
    index_to_label = config.labels

    with torch.no_grad():
        # Declare model and load pre-trained weights.
        tokenizer = AutoTokenizer.from_pretrained(config.model_fn, use_fast=True)
        model_loader = AutoModelForSequenceClassification
        config_model = AutoConfig.from_pretrained(config.model_fn)
        model = model_loader.from_pretrained(
            config.model_fn,
            num_labels=config.num_classes,
            config=config_model,
        )
        model.load_state_dict(config.best_model_path)

        if config.gpu_id >= 0:
            model.cuda(config.gpu_id)
        device = next(model.parameters()).device

        model.eval()

        y_hats = []
        for idx in range(0, len(lines), config.batch_size):
            mini_batch = tokenizer(
                lines[idx:idx + config.batch_size],
                padding=True,
                truncation=True,
                return_tensors="pt",
            )

            x = mini_batch['input_ids']
            x = x.to(device)
            mask = mini_batch['attention_mask']
            mask = mask.to(device)

            # Take feed-forward
            y_hat = F.softmax(model(x, attention_mask=mask).logits, dim=-1)

            y_hats += [y_hat]
        # Concatenate the mini-batch wise result
        y_hats = torch.cat(y_hats, dim=0)
        # |y_hats| = (len(lines), n_classes)

        probs, indice = y_hats.cpu().topk(config.top_k)
        # |indice| = (len(lines), top_k)

        result = []
        for i, line in enumerate(lines):
        	# classification probability, 광고 여부, 분류한 텍스트를 담아 반환.
            row = [float(probs[i][0]), index_to_label[int(indice[i][0])], line]
            result.append(row)
        return result
