# ROSCOG
_Developing a ROS-based Cognitive Architecture for AGI in Humanoid Robots. Using Deep Neural Networks for learning._

**Timeline:**

Mental Representations:

A mental representation, also called cognitive representation, in philosophy of mind, cognitive psychology, and neuroscience is a hypothetical internal cognitive symbol that represents external reality. [ya]

roslaunch cogarch diagnostics.launch 
#different modes: ON [awake (autonomous), diagnostics, sleep (minimal power)] | OFF [dead]

Inspired by human mental representations, the proposed framework also incorporates this for a humanoid robot's mind. Similar to the concept of life and death in humans, a robot has two basic modes: it can be OFF, where it's electromechanical parts are not being powered by electricity or it can be ON. In its ON state, it is switched on and the battery is being accessed. Furthermore, the ON state contains mental representations: Awake, Diagnostics, Robot and Asleep.

Awake Mode: Autonomous, Learning, Biological Fitness, Maslow Hierarchy of Needs, Personality
Robot: Domain-Role: Process NLP Input, Load Memory/Experience, assume role, perform/act.
Diagnostics: Control Mode, adjust memory, beliefs revision 
Asleep Mode: minimal power, repair process, charge battery, data defragment, LTM/Belief Revision

#### Procedure:

Use ROSCOG to produce a POMDP for an agent. Use a DQN for decision-making and reinforcement learning.
Using Probablisitc Programming with Hypergraphs.

Tools: Python + ProbLog

`please dont steal my ideas/work, i want to publish research on this as this is my thesis, and eventually make a career out of this.
contact me to collaborate instead ?`

bibliography:
[ya] Morgan, Alex (2014). "Representations Gone Mental" (PDF). Synthese 191.2: 213–44.
