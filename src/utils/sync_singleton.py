import threading


class SyncSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    if hasattr(cls._instance, "_initialize"):
                        cls._instance._initialize(*args, **kwargs)
        return cls._instance

    # 同期用の初期化メソッド（オプション）
    # def _initialize(self, *args, **kwargs):
    #     pass
