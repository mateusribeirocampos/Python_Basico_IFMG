import null as null

var = {
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d6df62f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Informe os 3 lados do triângulo: \n",
      "Lado 1 = 2\n",
      "Lado 2 = 3\n",
      "Lado 3 = 4\n",
      "Triângulo escaleno\n"
     ]
    }
   ],
   "source": [
    "print('Informe os 3 lados do triângulo: ')\n",
    "a = float (input('Lado 1 = '))\n",
    "b = float (input('Lado 2 = '))\n",
    "c = float (input('Lado 3 = '))\n",
    "if(a > b + c) or (b > a + c) or (c > a + b):\n",
    "    print('Triângulo inválido')\n",
    "else:\n",
    "    if (a == b) and (b == c):\n",
    "        print('Triângulo equilátero')\n",
    "    elif (a == b) or (b == c) or (a == c):\n",
    "        print('Triângulo isósceles')\n",
    "    else:\n",
    "        print('Triângulo escaleno')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0174c81a",
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
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
