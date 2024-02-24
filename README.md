# Password Generator

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Language](https://img.shields.io/badge/Python-v3.10+-yellow)
![Technology](https://img.shields.io/badge/JSON-Config-skyblue)

This repository hosts a streamlined password generator capable of producing secure, random passwords of any desired
length. Crafted in Python, this versatile tool functions both as an independent script and as an importable module for
integration into various Python-based applications.

### How to Run

To operate the password generator independently, execute the `password_generator.py` script via the command line. For
instance:

```bash
python password_generator.py
```

This script produces a secure, random password determined by the `password_length` parameter specified in
the `config.json` file.

### Future Development

The script is fully operational, yet it holds the potential for several future upgrades to elevate its functionality:

* **Integrate Cryptographic Hashing**: Infusing the password generator with cryptographic hashing will significantly
  bolster
  its security measures.
* **Incorporate a Password Strength Evaluator**: A built-in tool to assess the robustness of the generated passwords
  would
  be a valuable addition.
* **Allow Definition of The Number of Passwords**: Enabling the user to specify the number of passwords to generate in a
  single run would enhance the tool’s flexibility.
* **Develop a Graphical User Interface (GUI)**: Crafting a user-friendly GUI would greatly enrich the overall user
  interaction, making the tool more accessible to a wider audience.

### How to Contribute

Contributions are always welcome! Here's how you can get involved:

* Report any bugs or issues you encounter.
* Suggest new features or enhancements to improve the password generator.
* Submit pull requests with code improvements or fixes.

We appreciate your contributions and feedback to make this project better!

### License

This project is released without a license. You are free to use it for any purpose.

**Happy Coding!**