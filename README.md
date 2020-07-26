Udacity's "Computer Vision Nanodegree"  included lessons and quizzes on CNN, RNN, LSTMs, Attention mechanism, (Graph) SLAM, and among other techniques. And, it required to pass the review of 3 capstone projects in Pytorch to <a href="https://confirm.udacity.com/9QK9JDSF">graduate</a>.

## Projects:

### Facial Key-points detection
A CNN was defined and trained on Youtube Faces Dataset to identify 68 facial key-points. Using Haar cascades face was detected. Facial keypoints were predicted using the trained model. (Fun filters and cooling glasses made this project even cooler!)

### Image captioning
A pretrained ResNet extended with untrained linear layers was trained on the MS COCO dataset. It encoded the features of the input image and an RNN (with LSTMs) was employed as a decoder to generate captions on new input images. Generated captions were quite accurate and funny.

### Landmark Detection and Tracking
Using Graph SLAM, system equations of the robot moving in a generated environment were computed. It is interesting to note that with only data from sensors and movement the 2D world was mapped.

The peer-to-peer discussions on Udacity's community slack group about these and other interesting topics in ML made it a wholesome experience.
