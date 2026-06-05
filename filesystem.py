class FakeFileSystem:
    def __init__(self):
        self.files = {
            "/": ["home", "var", "etc", "logs.txt"],
            "/home": ["user", "docs", "photos"],
            "/home/user": ["notes.txt", "todo.txt"],
        }

    def list_dir(self, path):
        return self.files.get(path, ["Invalid path"])

    def read_file(self, path):
        fake_data = {
            "notes.txt": "Remember: this is only a simulation.",
            "todo.txt": "- Learn Python\n- Build simulator\n- Add UI effects",
            "logs.txt": "[SYSTEM] All systems operational",
        }
        return fake_data.get(path.split("/")[-1], "File not found")
