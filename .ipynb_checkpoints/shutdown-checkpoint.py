{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "13301c82-6050-410b-87da-b8ef7228e8b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import platform\n",
    "\n",
    "system = platform.system()\n",
    "\n",
    "if system == \"Windows\":\n",
    "    os.system(\"shutdowm /s /t 0\")\n",
    "elif system == \"Linux\":\n",
    "    os.system(\"sudo shutdown now\")\n",
    "else:\n",
    "    print(\"The operating system is not running.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c109ca85-aa6b-467c-a6f6-fb3ffcbee25e",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
