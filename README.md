# 📈 Compound Interest Calculator (Simulador de Juros Compostos)

> A robust Command Line Interface (CLI) application developed in Python to simulate, track, and visualize the power of compound interest over time.

## 💡 Introduction

As an Information Systems student passionate about the intersection of technology, data analysis, and the financial market, I developed this project to solve a real-world problem: accurately visualizing how long-term investments and consistent contributions grow. 

This project serves as a practical application of Python fundamentals, bridging the gap between mathematical logic and software engineering. It was built with a focus on clean code, modular architecture, and user experience within the terminal.

## 🎯 What the Project Does

The **Compound Interest Calculator** empowers users to project their financial future. Instead of just returning a final number, the application acts as an analytical tool that:
* Takes user inputs for initial capital, monthly deposits, annual interest rates, and the total investment period.
* Calculates the exact monthly yield and progressive capital accumulation.
* Renders a highly formatted, easy-to-read table directly in the terminal showing the month-by-month evolution of the portfolio.
* **Automates Reporting:** Features an export function that generates a well-structured `.txt` file containing the full simulation data for external review or record-keeping.

## 🚧 Development Journey & Overcoming Challenges

Building this project was a significant stepping stone in solidifying my programming logic. During development, I tackled two major technical hurdles:

1. **Financial Mathematical Logic:**
   Implementing the compound interest formula required adapting annual rates to precise monthly equivalents. I had to ensure the logic `taxa_mensal = (1 + tjuros_anual/100)**(1/12) - 1` was accurately applied before compounding the balance with the new monthly deposits. Ensuring mathematical precision in the floating-point calculations was a critical learning curve.

2. **Data Structure Management (Dictionaries within Lists):**
   To generate the step-by-step report, I needed to store the state of the investment for *each month*. I solved this by dynamically creating dictionaries containing the monthly data (`rendimento`, `deposito`, `total_juros`, etc.) and appending them to a main `lista_resultado` during the `for` loop iteration. Managing this state and correctly clearing/updating the list for consecutive simulations taught me a lot about memory management and data structures in Python.

## 🛠️ Technologies Used

* **Python 3.13:** Core language used for all logic and scripting.
* **Standard Libraries (`os`, `time`):** Utilized for cross-platform terminal clearing (`cls` / `clear`) and managing UX delays to make the interface feel responsive and deliberate.
* **Modular Architecture:** The project is divided into an `app/` package containing `calculos.py` (business logic) and `interface.py` (view/presentation layer), ensuring the code is scalable and maintainable.

## ⚙️ How to Run the Project

Follow these steps to run the simulation on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Calculadora_JurosCompostos.git](https://github.com/your-username/Calculadora_JurosCompostos.git)
    ```
2. Navigate to the project directory:
    ```Bash
    cd Calculadora_JurosCompostos
    ```
3. Execute the main script:
    ```Bash    
    python main.py
    ```

    *(Ensure you have Python installed. No external virtual environments or PIP packages are required as it uses standard libraries).*

Developed with 💻 and ☕ by Felipe César Martins

