using System;

namespace Bank
{
    enum AccountTypes
    {
        Savings,
        Checking,
        Business,
         
    }
    

    class BankAccount
    {

        private int _accountNumber;
        private string _ownerName;
        private double _balance;
        private AccountTypes _accountType;
        private bool _isActive;
        private List<string> _transactionHistory;
        public int AccountNumber { get; }
        public string OwnerName
        {
            get { return _ownerName; }
            set
            { 
                if (string.IsNullOrWhiteSpace(value)) 
                {
                    _ownerName = "Unknown";
                }
                else
                {
                    _ownerName = value;
                }
            }
        }
        public double Balance
        {
            get { return _balance; }
            private set
            {
                if (value < 0.0)
                {
                    _balance = 0.0;
                }
                else
                {
                    _balance = value;
                }
            }
        }

        public AccountTypes AccountType
        {
            get { return _accountType; }
            set 
            {
                _accountType = value; 
            }
        }
        public bool IsActive
        {
            get { return _isActive;}
            set { _isActive = value; }
        }

        public BankAccount(int accountNumber, string ownerName)
            :this(accountNumber, ownerName, 0.0, AccountTypes.Checking)
        {

        }

        public BankAccount(int accountNumber, string ownerName, double balance, AccountTypes accountType)
        {
            AccountNumber = accountNumber;
            OwnerName = ownerName;
            Balance = balance;
            AccountType = accountType;
            IsActive = true;
            _transactionHistory = new List<string>();
        }

        public override string ToString()
        {
            return $"Account #{_accountNumber} | Owner: {_ownerName} | Balance: ${_balance:F2} | Type: {_accountType}";
        }

        public void Deposit(double amount)
        {
            if (amount < 0.0)
            {
                Console.WriteLine("Warning: amount was less than 0.");
                Balance += amount;
            }
            else
            {
                Balance += amount;
                Console.WriteLine("The anount was added succesfully");
            }
        }
        public bool Withdraw(double amount)
        {
            if (amount > Balance)
            {
                Console.WriteLine("Error: The amount was more than the balance");
                return false;
            }
            if (amount < 0)
            {
                Console.WriteLine("Error: THe amount was less than 0.");
                return false;
            }
            Balance -= amount;
            return true;
            
        }


    }
    class Manager
    {

        static void Main()
        {
            BankAccount b1 = new BankAccount(1, "Elazar", 1000, AccountTypes.Savings);
            b1.Withdraw(-100);
            Console.WriteLine(b1);
            
        }

    }

    

}