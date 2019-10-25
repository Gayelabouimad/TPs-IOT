# TPs-IOT
The repo will contain our Tps

## TP1 - Exploring LoRa Technology - Performance Evaluation

Tasks :
Questions 
- [x] What are the advantages of the LoRa modulation?
- [x] How LoRa is compatible with LPWAN requirements and constraints?

### 1. Setting the Lab

#### 1.1. Hardware Platform
- [x] Give the characteristics of the Arduino you are using: model, number of pins, type of pins, memory sizes, etc.
- [x] Give the main characteristics of the LoRa shield from Dragino (www.dragino.com).
- [x] What type of Antenna are you using? Explain the corresponding characteristics.
- [x] Give an estimated cost of your devices.

### 2. Theoretical Study

Already DONE!!

- [x] What is the relation between processing gain and spreading factor in LoRa modulation?
- [x] How does the spreading factor impact the coverage of a LoRa transmitter?
- [x] What is the transmission bit rate for each of the following configurations of your LoRa device? Explain your computation.
        Configuration 1: channel bandwidth = 125 kHz, spreading factor = 7, coding rate = 4/5
        Configuration 2: channel bandwidth = 500 kHz, spreading factor = 7, coding rate = 4/5
        Configuration 3: channel bandwidth = 125 kHz, spreading factor = 12, coding rate = 1/2
- [x] Compute the receiver sensitivity, assuming the following parameters: channel bandwidth = 125 kHz, spreading factor = 7, coding rate = 4/5, bit error rate (BER) target = 10-4, and receiver noise figure = 6 dB. Refer to this article to determine the mapping between the BER and the SNR.
- [x] Compare the computed sensitivity to that provided by the Semtech Application Note AN1200.22 for the same parameters.


### 3. Configuring and Running the Lab

Already DONE!!

Note : Groupe 9	--> freq = 868.3

### 4. Performance Evaluation

#### 4.1. Time on Air

- [x] Measure the time on Air
- [x] Implement client function using python
- [x] Modify Params and track changes (repeat 100 times)

- [x] Do the theoretical computation
- [x] add theoretical values to experimental graph
- [x] Describe the scenarios you used for assessing the impact of the different parameters on the ToA.
- [x] Join commented extracts of your code and raw data in attached files.
- [x] Visualise the experimental results by plotting the ToA as a function of each one of the different parameters.
- [x] Analyze the obtained results and compare with the theoretical computations. You can superpose the theoretical results and the experimental ones on the same graph.



## TP2 - Exploring LoRa Technology - Collisions and Packet Delivery Ratio

The deliverable should include the answers to the questions in IoT Labs: Exploring LoRa

Section 4.2