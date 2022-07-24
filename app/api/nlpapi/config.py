import os


class Config:

    def __init__(
        self, model_fn : str,
        lines : list,
        gpu_id : int = -1,
        batch_size : int = 8,
        num_classes : int = 2,
        top_k : int = 1, 
        labels : list = ["광고", "정치"],
        best_model_path : str = "./trained_model/bert_clean.tok.slice.pth"
    ):
    	# model full name. 모델 저장 경로
        self.model_fn = model_fn
        # cuda 사용 시, gpu id
        self.gpu_id = gpu_id
        self.batch_size = batch_size
        # 분류하고자 하는 블로그 text들
        self.lines = lines
        # probability 상위 몇 개를 출력할 것인지
        self.top_k = top_k

        self.num_of_classes = num_classes
        self.labels = labels
        assert(len(self.labels) == self.num_of_classes)

        self.best_model_path = best_model_path
        # assert if file exists ast best_model_path
        assert(os.path.exists(self.best_model_path))
