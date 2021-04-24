{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5cbf503",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import the necessary packages\n",
    "from pytesseract import Output\n",
    "import pytesseract\n",
    "import argparse\n",
    "import cv2\n",
    "# construct the argument parser and parse the arguments\n",
    "ap = argparse.ArgumentParser()\n",
    "ap.add_argument(\"-i\", \"--image\", required=True,\n",
    "    help=\"path to input image to be OCR'd\")\n",
    "ap.add_argument(\"-c\", \"--min-conf\", type=int, default=0,\n",
    "    help=\"mininum confidence value to filter weak text detection\")\n",
    "args = vars(ap.parse_args())\n",
    "\n",
    "image = cv2.imread('IMG_1472.png')\n",
    "rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)\n",
    "results = pytesseract.image_to_data(rgb, output_type=Output.DICT)\n",
    "\n",
    "for i in range(0, len(results[\"text\"])):\n",
    "# extract the bounding box coordinates of the text region from\n",
    "# the current result\n",
    "    x = results[\"left\"][i]\n",
    "    y = results[\"top\"][i]\n",
    "    w = results[\"width\"][i]\n",
    "    h = results[\"height\"][i]\n",
    "# extract the OCR text itself along with the confidence of the\n",
    "# text localization\n",
    "    text = results[\"text\"][i]\n",
    "    conf = int(results[\"conf\"][i])\n",
    "\n",
    "# filter out weak confidence text localizations\n",
    "if conf > args[\"min_conf\"]:\n",
    "        # display the confidence and text to our terminal\n",
    "    print(\"Confidence: {}\".format(conf))\n",
    "    print(\"Text: {}\".format(text))\n",
    "    print(\"\")\n",
    "\t# strip out non-ASCII text so we can draw the text on the image\n",
    "\t\t# using OpenCV, then draw a bounding box around the text along\n",
    "\t# with the text itself\n",
    "    text = \"\".join([c if ord(c) < 128 else \"\" for c in text]).strip()\n",
    "    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)\n",
    "    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,\n",
    "        1.2, (0, 0, 255), 3)\n",
    "# show the output image\n",
    "cv2.imshow(\"Image\", image)\n",
    "cv2.waitKey(0)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
