```python
# Importing necessary libraries
from flask import Flask
import tensorflow as tf
import torch

# Creating a Flask application
app = Flask(__name__)

# Checking TensorFlow version
def check_tf_version():
    print("TensorFlow version: ", tf.__version__)

# Checking PyTorch version
def check_torch_version():
    print("PyTorch version: ", torch.__version__)

# Running the Flask application
if __name__ == "__main__":
    app.run(debug=True)
    check_tf_version()
    check_torch_version()
```