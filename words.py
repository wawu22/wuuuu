from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = "Wolf Warrior 2 is a 2017 Chinese action film directed by Wu Jing, who also starred in the lead role. The film co-stars Celina Jade, Frank Grillo, Hans Zhang, and Wu Gang. The film is a sequel to the 2015 s Wolf Warrior. The film tells a story of a loose cannon Chinese soldier named Leng Feng who takes on special missions around the world. In this sequel, he finds himself in an African country protecting medical aid workers from local rebels and vicious arms dealers. received general praise for its patriotic plot, special effects, action sequences and the performances of the cast. It was a massive commercial success and has become the highest-grossing Chinese film ever released. The film broke numerous box office records, including the biggest single-day gross for a Chinese film as well as the fastest film to cross RMB 2 billion, 3 billion, 4 billion and 5 billion box office marks.Wolf Warrior 2 is a 2017 Chinese action film directed by Wu Jing, who also starred in the lead role. The film co-stars Celina Jade, Frank Grillo, Hans Zhang, and Wu Gang. The film is a sequel to the 2015 s Wolf Warrior. The film tells a story of a loose cannon Chinese soldier named Leng Feng who takes on special missions around the world. In this sequel, he finds himself in an African country protecting medical aid workers from local rebels and vicious arms dealers. received general praise for its patriotic plot, special effects, action sequences and the performances of the cast. It was a massive commercial success and has become the highest-grossing Chinese film ever released. The film broke numerous box office records, including the biggest single-day gross for a Chinese film as well as the fastest film to cross RMB 2 billion, 3 billion, 4 billion and 5 billion box office marks.War Wolf" is a modern military war film directed by Wu Jing. The film is starring Wu Jing, Yu Nan, Ni Dahong, Scott Akins and Zhou Xiaoou.
The film belongs to China's first 3D action war movie, which took seven years to build. The "War Wolf" truly presents a Sino-foreign border war, and also allows the special forces team and high-energy fighters who are called "Oriental Wolf" to land on the big screen for the first time. It tells the story of a small man who grew up to be a lonely hero who saved the destiny of the country and the nation.
The film was released nationwide on April 2, 2015.
On June 20th, 2015, "War Wolf" won four awards in the best action movie, best action actor, best stunt, best fight scene design at Jackie Chan Action Movie Week. [1] 
On August 6, 2016, the 20th China Ding Awards Organizing Committee announced the list of the top 50 films in Hong Kong. The film "War Wolf" topped the list. [2] On September 7th, the film won the 20th China Ding Award Best Screenplay Award, Best New Director Director Award, Best Action Film Guide Award, Best Film Producer Award, and Film Satisfaction Survey . [3] On September 24th, the film won the Outstanding Film and Best Newcomer Award at the 33rd Popular Film Awards."



cloud = WordCloud(background_color="white", mask = our_mask).generate(text)

plt.imshow(cloud)
plt.axis('off')
plt.show()
