from threading import Semaphore, Lock

class BoundedBlockingQueue(object):
    # Semaphore는 하나의 counter처럼 작동한다.
    # 여러 개 스레드가 동시에 접근할 때, 접근순서에 따라 결과가 다르다는 문제점을 해결할 요량으로 사용

    def __init__(self, capacity: int):
        # 저장할 수 있는 총 용량
        self.c = capacity
        self.pulling = Semaphore(0)
        # c만큼의 count
        # acquire로 count 감소, release로 count 증가.
        # count가 0인 상태에서 acquire = block된다.
        self.pushing = Semaphore(self.c)
        # lock은 acquire = lock / release = unlock.
        self.editing = Lock()
        self.data = []
    def enqueue(self, element: int) -> None:
        self.pushing.acquire() # count 1 감소
        self.editing.acquire() # unlock -> lock상태로 변경
        self.data.append(element)
        self.editing.release()
        # pushing이 아니라 pulling을 release.
        # pulling semaphore의 count 증가 -> dequeue 명령어로 데이터 꺼낼 수 있도록.
        self.pulling.release()
    
    def dequeue(self) -> int:
        # deque를 위한 semaphore count 1 감소
        self.pulling.acquire()
        self.editing.acquire()
        item = self.data.pop(0)
        self.editing.release()
        # 데이터 삽입을 위한 count 1 증가
        self.pushing.release()
        return item
    
    def size(self) -> int:
        return len(self.data)