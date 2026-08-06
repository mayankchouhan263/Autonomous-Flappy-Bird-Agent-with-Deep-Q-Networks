# Autonomous Flappy Bird Agent using Deep Q-Networks (DQN)

An autonomous Flappy Bird agent trained using **Deep Q-Networks (DQN)**, a reinforcement learning algorithm that learns optimal actions through interaction with the environment. The project uses **PyTorch** for neural network implementation and **Flappy Bird Gymnasium** as the simulation environment.

---

## Features

- Deep Q-Network (DQN) implementation
- Experience Replay Memory
- Target Network synchronization
- Epsilon-Greedy exploration strategy
- Automatic model checkpointing
- Configurable hyperparameters using YAML
- Training and evaluation modes
- Support for CPU, CUDA, and Apple MPS

---

## Project Structure

```text
Autonomous-Flappy-Bird-Agent-with-Deep-Q-Networks/
│
├── agent.py                 # Training and evaluation script
├── dqn.py                   # Deep Q-Network model
├── experience_replay.py     # Replay memory implementation
├── parameters.yaml          # Hyperparameter configuration
├── runs/                    # Saved models and training logs
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.10+
- PyTorch
- Gymnasium
- Flappy Bird Gymnasium
- PyYAML

Install all dependencies:

```bash
pip install -r requirements.txt
```

or install manually:

```bash
pip install torch
pip install gymnasium
pip install flappy-bird-gymnasium
pip install pyyaml
```

---

## Usage

### Train the Agent

Run the following command to start training:

```bash
python agent.py flappybirdv0 --train
```

During training, the agent learns by interacting with the environment. The best-performing model and training log are automatically saved in the `runs/` directory.

---

### Evaluate the Agent

After training, run:

```bash
python agent.py flappybirdv0
```

The trained model is automatically loaded from the `runs/` directory, and the agent plays the game using the learned policy.

---

## Output

Training generates the following files:

```text
runs/
├── flappybirdv0.pt      # Trained model
└── flappybirdv0.log     # Training log
```

---

## Hyperparameters

Training parameters are defined in `parameters.yaml`.

Available parameters include:

- Learning rate (`alpha`)
- Discount factor (`gamma`)
- Initial epsilon
- Minimum epsilon
- Epsilon decay
- Replay memory size
- Mini-batch size
- Reward threshold
- Target network synchronization rate

To experiment with different settings, add a new parameter set in `parameters.yaml` and use its name in place of `flappybirdv0` when running the program.

---

## Reinforcement Learning Pipeline

The agent follows the standard DQN workflow:

1. Observe the current game state.
2. Select an action using the epsilon-greedy policy.
3. Execute the action in the environment.
4. Store the experience in replay memory.
5. Sample a mini-batch of experiences.
6. Compute target Q-values using the target network.
7. Update the policy network using gradient descent.
8. Periodically synchronize the target network.
9. Save the best-performing model.

---

## Technologies Used

- Python
- PyTorch
- Gymnasium
- Flappy Bird Gymnasium
- NumPy
- PyYAML

---

## Future Improvements

- Double DQN (DDQN)
- Dueling DQN
- Prioritized Experience Replay
- Rainbow DQN
- TensorBoard integration
- Hyperparameter optimization
- Performance visualization

---

## Author

**Mayank Chouhan**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

---

## License

This project is released under the MIT License. Feel free to use, modify, and distribute it for educational and personal projects.
