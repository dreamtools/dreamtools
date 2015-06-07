from numpy import loadtxt
from pylab import *


# incoherent feedforward loop data is in incoherent_feedforward_loop.txt. The
# subnetwork p6/p7/p8 is independent of the rest of the networks so the
# model1.sbml could be used directly in copasi to generate these time course
# data set.

# Similarly the sub network related to p9 (autoregulation) is not affected by
# other genes so we can use the SBML as it stands.

# read the header and extract the relevant columns for p8


def get_header(filename):
    data = open(filename).read()
    header = [x for x in data.split("\n")[0].split("\t") if len(x)>0]
    assert header[0] == "#Time", "first element of the heade must be #Time (no space)"
    return header

header = get_header("TimeCourse1.txt")


data = loadtxt("TimeCourse1.txt")
time = data[:,0]
p8 = data[:,header.index("p8")]
p9 = data[:,header.index("p9")]
p7 = data[:,header.index("p7")]
p6 = data[:,header.index("p6")]
p1 = data[:,header.index("p1")]
p2 = data[:,header.index("p2")]
p3 = data[:,header.index("p3")]
p4 = data[:,header.index("p4")]
p5 = data[:,header.index("p5")]




# now plot the figure for p8
clf(); 
plot(time, p8, lw=2); 
grid(True);
xlabel("Time (seconds)",fontsize=16); 
ylabel("p8", fontsize=16); 
title("Incoherent feedforward loop", fontsize=18);
savefig("dream7_param_inc_feedforward_loop.png", dpi=140)


# cascade
clf(); 
plot(p7[0:39], p3[0:39], lw=2); 
hold(True);
plot(p7[0:39], p7[0:39], '--k' ); 
grid(True);
xlabel("p7",fontsize=16); 
ylabel("p3", fontsize=16); 
title("Regulatory Cascade", fontsize=18);
savefig("dream7_param_regulatory_cascade.png", dpi=140)



# now plot the figure for p8
clf(); 
plot(time, p2, lw=2); 
grid(True);
xlabel("Time (seconds)", fontsize=16); 
ylabel("p2", fontsize=16); 
title("Negative feedback", fontsize=18);
savefig("dream7_param_negative_feedback.png", dpi=140)



# now plot the figure for p1 positive feedback
clf(); 
plot(time, p1, lw=2); 
hold(True)
grid(True);
xlabel("Time (seconds)", fontsize=16); 
ylabel("p1", fontsize=16); 
title("Positive feedback", fontsize=18);
savefig("dream7_param_positive_feedback.png", dpi=140)



# now plot the figure for p1 positive feedback
clf(); 
plot(time, p9, lw=2); 
grid(True);
xlabel("Time (seconds)", fontsize=16); 
ylabel("p9", fontsize=16); 
title("Negative autoregulation", fontsize=18);
savefig("dream7_param_negative_autoregulation.png", dpi=140)






def TC1():
    header = get_header("TimeCourse1.txt")
    data = loadtxt("TimeCourse1.txt")
    time = data[:,0]
    p8 = data[:,header.index("p8")]
    p9 = data[:,header.index("p9")]
    p7 = data[:,header.index("p7")]
    p6 = data[:,header.index("p6")]
    p1 = data[:,header.index("p1")]
    p2 = data[:,header.index("p2")]
    p3 = data[:,header.index("p3")]
    p4 = data[:,header.index("p4")]
    p5 = data[:,header.index("p5")]


    for i, protein in enumerate([p1, p2, p3, p4, p5, p6, p7, p8, p9]):
        print("generating p%s" % str(i+1)); 
        clf(); 
        plot(time, protein, lw=2); 
        grid(True);
        xlabel("Time (seconds)", fontsize=16); 
        ylabel("p"+str(i+1), fontsize=16); 
        savefig("dream7_param1_p%s.png" % str(i+1), dpi=140)


def TC2():
    header = get_header("TimeCourse2.txt")
    data = loadtxt("TimeCourse2.txt")
    time = data[:,0]
    p8 = data[:,header.index("p8")]
    p9 = data[:,header.index("p9")]
    p7 = data[:,header.index("p7")]
    p6 = data[:,header.index("p6")]
    p1 = data[:,header.index("p1")]
    p2 = data[:,header.index("p2")]
    p3 = data[:,header.index("p3")]
    p4 = data[:,header.index("p4")]
    p5 = data[:,header.index("p5")]
    p10 = data[:,header.index("p10")]
    p11 = data[:,header.index("p11")]


    for i, protein in enumerate([p1, p2, p3, p4, p5, p6, p7, p8, p9 ,p10, p11]):
        print("generating p%s" % str(i+1)); 
        clf(); 
        plot(time, protein, lw=2); 
        grid(True);
        xlabel("Time (seconds)", fontsize=16); 
        ylabel("p"+str(i+1), fontsize=16); 
        savefig("dream7_param2_p%s.png" % str(i+1), dpi=140)


TC1()
TC2()
