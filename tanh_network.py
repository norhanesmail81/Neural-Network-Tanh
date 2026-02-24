{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "840ce4f6-28a9-4986-bd3d-c318db4ebfc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "323d2db3-6f7d-4c8b-a386-85f56460acb4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final Output of the Network:\n",
      "[[0.45987875]\n",
      " [0.67227315]]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Activation function\n",
    "def tanh(x):\n",
    "    return np.tanh(x)\n",
    "\n",
    "# Inputs (example)\n",
    "X = np.array([[0.05],\n",
    "              [0.10]])   # 2 inputs\n",
    "\n",
    "# Random weights in [-0.5, 0.5]\n",
    "W1 = np.random.uniform(-0.5, 0.5, (2, 2))  # Hidden layer\n",
    "W2 = np.random.uniform(-0.5, 0.5, (2, 2))  # Output layer\n",
    "\n",
    "# Bias values\n",
    "b1 = 0.5\n",
    "b2 = 0.7\n",
    "\n",
    "# Forward propagation\n",
    "\n",
    "# Hidden layer\n",
    "Z1 = np.dot(W1, X) + b1\n",
    "A1 = tanh(Z1)\n",
    "\n",
    "# Output layer\n",
    "Z2 = np.dot(W2, A1) + b2\n",
    "Output = tanh(Z2)\n",
    "\n",
    "# Print final output of the network\n",
    "print(\"Final Output of the Network:\")\n",
    "print(Output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70a8d6b6-8f2b-41ad-ad60-a0acd4c4ae7b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
