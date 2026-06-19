class TreeNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value) if self.value is not None else "·"