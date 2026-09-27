"""Build an independent practice pack around the user's supplied topic index.
Article links are retained as references, not represented as retrieved lesson text.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
outline=json.loads((ROOT/'docs/supplied-outline.json').read_text())
NOTES={}
def add(id,summary,concepts,takeaway,stem,options,why):
    NOTES[id]={'summary':summary,'concepts':[{'term':t,'definition':d} for t,d in concepts],
               'takeaway':takeaway,'scenario':{'prompt':stem,'options':options,'correctIndex':0,'explanation':why}}

# These notes and hypothetical questions are original supplemental material.
# They are not copied from the linked AllDayABA articles or any secure exam bank.
add('A.1', 'Scientific understanding progresses from describing observations to predicting relationships and demonstrating experimental control.', [
('Description','Systematically observe, measure, and report what occurs.'),
('Prediction','Use an observed relationship to anticipate an event; prediction alone does not establish causation.'),
('Control','Demonstrate that manipulating a variable reliably changes behavior under the conditions studied.')],
'Association supports prediction. An experimental demonstration is needed to support a causal claim.',
'A researcher finds that requests for help are more frequent during difficult assignments, but has not manipulated task difficulty. What level of understanding does this relationship support?',
['Prediction','Experimental control','Proof that difficulty causes every request','A functional analysis'],
'A measured relationship can support prediction. Without an experimental manipulation, the relationship does not demonstrate control.')
add('A.2','Behavior analysis uses a scientific worldview to look for lawful relationships and useful, evidence-based explanations.',[
('Determinism','Events have lawful relations to other events rather than occurring without relevant conditions.'),
('Empiricism','Base knowledge on systematic observation and measurement.'),
('Parsimony','Rule out simpler adequate explanations before accepting more complex ones.'),
('Pragmatism','Evaluate explanations and practices partly by their practical usefulness.'),
('Selectionism','Consequences select and maintain patterns across biological, individual, and cultural histories.')],
'Do not confuse collecting evidence (empiricism) with preferring an economical adequate explanation (parsimony).',
'Before attributing a learner’s missed responses to an elaborate hidden process, an analyst checks whether the instructions were audible and understood. Which assumption is most directly illustrated?',
['Parsimony','Pragmatism alone','Randomness','Mentalism'],
'The analyst first checks simpler adequate explanations. Parsimony does not mean choosing a simple explanation when evidence contradicts it.')
add('A.3','Radical behaviorism treats private events as part of behavior rather than excluding them from scientific consideration.',[
('Private events','Events such as thinking or feeling that are directly accessible to the person but not equally observable by others.'),
('Radical behaviorism','A philosophy that includes public and private behavior and examines their relations to environmental and biological conditions.')],
'Including thoughts and feelings is not the same as using them as unexplained final causes.',
'A clinician acknowledges a person’s reported anxiety while also examining the conditions under which avoidance occurs. Which interpretation best fits radical behaviorism?',
['Private events can be studied as behavior in context','Private events must be denied','Reported feelings explain behavior without further analysis','Only visible movement is behavior'],
'Radical behaviorism includes private events; it does not treat a feeling label as a sufficient explanation that ends inquiry.')
add('A.4','The field includes a philosophy, basic research, applied research, and professional practice. They are related but not interchangeable.',[
('Experimental analysis of behavior','Basic research on behavioral processes, often under tightly controlled conditions.'),
('Applied behavior analysis','Research that applies behavioral principles to socially important behavior and evaluates functional relationships.'),
('Professional practice','Delivering behavior-analytic services informed by the science and professional standards.')],
'Classify the activity by its purpose, not just its setting or the person’s job title.',
'A laboratory systematically changes reinforcement schedules to investigate a basic behavioral process without a specific service-delivery goal. Which branch is most directly represented?',
['Experimental analysis of behavior','Professional service delivery','Credential administration','Applied clinical treatment by definition'],
'The central purpose is basic experimental research on a behavioral process.')
add('A.5','The dimensions of ABA describe the character of applied behavior-analytic work, not a checklist of treatment techniques.',[
('Applied and behavioral','Address socially important behavior and measure what people actually do.'),
('Analytic and technological','Demonstrate a convincing relationship and describe procedures clearly enough to replicate.'),
('Conceptually systematic, effective, and generality','Connect procedures to principles, produce meaningful change, and examine change across time, settings, or behaviors.')],
'Replication-ready instructions concern the technological dimension; durable or transferred change concerns generality.',
'A report describes every intervention step so another trained practitioner can implement it consistently. Which dimension is highlighted?',
['Technological','Generality','Applied','Effective'],
'Technological refers to sufficiently precise, complete procedural descriptions.')

add('B.1','Separate the broad activity being analyzed from a single instance and from a group of responses with a common function.',[
('Response','One instance of behavior.'),('Response class','A group of responses that share a relevant property, often a common effect on the environment.')],
'Responses can look different and still belong to the same functional response class.',
'A learner says “help,” raises a hand, and taps a help icon. Each response reliably produces assistance. What can these different actions form?',
['A functional response class','A single response instance','A stimulus class only','Respondent extinction'],
'Different response forms can belong to a functional class when they produce the same kind of environmental effect.')
add('B.2','Stimuli are environmental events or properties. A stimulus class groups stimuli by relevant shared features or effects.',[
('Stimulus','An environmental change or feature that can affect an organism.'),('Stimulus class','A set of stimuli grouped by physical features, temporal relations, or behavioral function.')],
'A stimulus is not the response it occasions.',
'A printed STOP sign, a spoken “stop,” and a red signal all occasion stopping in a trained learner. How could they be grouped?',
['As a functional stimulus class','As one motor response','As a fixed-ratio schedule','As identical physical stimuli'],
'These stimuli differ physically but may share a behavioral function.')
add('B.3','Respondent and operant processes describe different behavior–environment relations.',[
('Respondent conditioning','A previously neutral stimulus acquires an eliciting function through pairing with another stimulus.'),('Operant conditioning','Consequences alter the future likelihood of behavior under relevant conditions.')],
'An eliciting stimulus–response relation differs from a response–consequence relation.',
'A previously neutral sound is repeatedly paired with a stimulus that elicits blinking. Eventually the sound alone elicits blinking. Which process is illustrated?',
['Respondent conditioning','Operant extinction','Negative punishment','Response chaining'],
'The sound acquires an eliciting function through pairing, rather than through a consequence contingent on blinking.')
add('B.4','Reinforcement is defined by an increase in future behavior, not by whether someone intended to reward it.',[
('Positive reinforcement','A stimulus is added following behavior, and that behavior subsequently increases.'),('Negative reinforcement','A stimulus is removed, postponed, or avoided following behavior, and that behavior subsequently increases.')],
'Positive means addition; negative means removal. Reinforcement means behavior increases.',
'A driver fastens a seat belt, the warning tone stops, and fastening the belt becomes more likely on later trips. What process is illustrated?',
['Negative reinforcement','Positive punishment','Negative punishment','Respondent extinction'],
'The response removes the tone and increases in the future. Both parts are needed to identify negative reinforcement.')
add('B.5','Punishment describes a reduction in future behavior following a consequence. The label depends on the measured effect.',[
('Positive punishment','A stimulus is added after behavior and future behavior decreases.'),('Negative punishment','A stimulus is removed after behavior and future behavior decreases.')],
'An unpleasant consequence is not automatically punishment; behavior must subsequently decrease.',
'A game removes a player’s earned points after a rule violation, and violations subsequently decrease. Which process is described?',
['Negative punishment','Negative reinforcement','Positive reinforcement','Automatic reinforcement'],
'Something is removed, and future violations decrease. This is a conceptual example, not a recommendation to use punishment.')
add('B.6','A consequence may depend on another person or occur directly through the response’s interaction with the environment.',[
('Socially mediated contingency','Another person delivers or mediates the relevant consequence.'),('Automatic contingency','The relevant consequence occurs without another person delivering it.')],
'Automatic does not mean unconscious; it describes how the consequence is produced.',
'A person adjusts a desk lamp, directly improving the light on a page. This consequence makes similar adjustments more likely. No one else participates. What is the best classification?',
['Automatic reinforcement','Socially mediated reinforcement','Socially mediated punishment','A verbal prompt'],
'The response directly produces the relevant environmental change without another person delivering it.')
add('B.7','Reinforcers are identified by their effects. Their histories help distinguish unconditioned, conditioned, and generalized conditioned reinforcers.',[
('Unconditioned reinforcer','A stimulus whose reinforcing effectiveness does not depend on a specific learning history.'),('Conditioned reinforcer','A stimulus that acquired reinforcing effectiveness through learning.'),('Generalized conditioned reinforcer','A conditioned reinforcer associated with multiple other reinforcers.')],
'Preference can suggest candidates; an increase in behavior demonstrates a reinforcing effect.',
'A token can be exchanged for several different activities and items and has acquired reinforcing effects. What is the best classification?',
['Generalized conditioned reinforcer','Unconditioned reinforcer','Discriminative stimulus by definition','Respondent punisher'],
'Association with multiple backup reinforcers supports classifying the token as a generalized conditioned reinforcer.')
add('B.8','Punishers are classified by behavioral effects and learning history, not simply by their physical appearance.',[
('Unconditioned punisher','A stimulus whose punishing effectiveness does not require a specific learning history.'),('Conditioned punisher','A stimulus that acquired punishing effectiveness through learning.'),('Generalized conditioned punisher','A conditioned punisher associated with multiple other punishers.')],
'The same event can have different effects for different people and contexts.',
'A neutral warning signal acquires a suppressive effect after repeated association with events that decrease responding. Which category fits the learned effect?',
['Conditioned punisher','Unconditioned reinforcer','Neutral stimulus with no learned function','Variable-interval schedule'],
'The question describes acquired, rather than unlearned, punishing effectiveness. This is classification, not intervention guidance.')
add('B.9','Simple schedules specify when a response can produce reinforcement.',[
('Ratio schedules','Reinforcement depends on a response count. Fixed ratios use a constant requirement; variable ratios vary around an average.'),('Interval schedules','Reinforcement follows the first qualifying response after a time interval. Fixed intervals are constant; variable intervals vary.')],
'An interval schedule still requires a response. Time-based delivery does not.',
'The first qualifying response after each varying interval produces reinforcement. Which schedule is described?',
['Variable interval','Variable ratio','Fixed time','Fixed ratio'],
'The elapsed interval varies, and a response is still required after it elapses.')
add('B.10','Compound schedules combine simple schedules, differing in whether components are simultaneous, signaled, or sequential.',[
('Concurrent schedules','Two or more schedules are available at the same time for different response options.'),('Multiple versus mixed schedules','Components alternate; multiple schedules have distinct correlating stimuli, while mixed schedules do not.'),('Chained schedule','Distinct, signaled components must be completed in sequence; the terminal component produces the terminal reinforcer.')],
'Look first for simultaneous versus successive components, then for signals and sequence requirements.',
'Two reinforcement schedules alternate. A green light signals one component and a blue light signals the other. Which arrangement is described?',
['Multiple schedule','Mixed schedule','Concurrent schedule','Unsignaled single schedule'],
'Alternating components with distinct correlated stimuli define a multiple schedule.')
add('B.11','Extinction depends on the kind of behavior–environment relation that previously maintained responding.',[
('Operant extinction','Discontinue the reinforcement that previously maintained a response.'),('Respondent extinction','Present the conditioned stimulus without the unconditioned stimulus, reducing the conditioned response over repeated presentations.')],
'Extinction is not a synonym for ignoring. The maintaining reinforcer determines the procedure.',
'A laboratory response previously produced a pellet. The response no longer produces pellets, and responding decreases over time. Which process is illustrated?',
['Operant extinction','Negative punishment by definition','Respondent conditioning','Positive reinforcement'],
'The previously response-contingent reinforcer is discontinued. No previously earned reinforcer is removed.')
add('B.12','Stimulus control describes differences in responding in the presence of different antecedent stimuli because of a learning history.',[
('Discriminative stimulus (SD)','An antecedent correlated with reinforcement being available for a particular response.'),('Stimulus control','A response occurs differentially in relation to antecedent stimuli because of differential consequences in the past.')],
'An SD signals differential availability; it does not primarily change the value of the reinforcer.',
'A help light signals that an instructor is available. A student’s requests are reinforced when it is on but not when it is off. Requests become more frequent when it is on. What is demonstrated?',
['Stimulus control','Unconditioned responding','Response generalization','Punishment without learning'],
'The antecedent light becomes correlated with reinforcement availability for requesting help.')
add('B.13','Discrimination is differential responding to different stimuli following relevant learning.',[
('Stimulus discrimination','Respond differently to stimuli based on a history of differential consequences.'),('Discrimination training','Arrange different consequences for responding in the presence of different antecedent stimuli.')],
'Discrimination concerns differences; generalization concerns responding beyond the trained conditions.',
'A learner selects the recycling bin for paper but the waste bin for a nonrecyclable wrapper after training. What is most directly demonstrated?',
['Stimulus discrimination','Respondent extinction','Undifferentiated responding','Response maintenance only'],
'Different stimuli occasion different responses in accordance with the training history.')
add('B.14','Generalization extends learning beyond the specific stimuli or responses directly trained.',[
('Stimulus generalization','A learned response occurs in the presence of other relevant, untrained stimuli.'),('Response generalization','Untrained responses occur that are functionally related to the trained response.')],
'Ask what changed: the situation or stimulus, or the form of the response?',
'After learning to say “hello,” a learner independently uses “hi” and a wave in the same greeting situation. What type of generalization is highlighted?',
['Response generalization','Stimulus discrimination','Respondent extinction','A fixed-interval schedule'],
'The response forms vary beyond the trained form while serving the same greeting function.')
add('B.15','Maintenance concerns continued behavior over time after instruction or intervention has been reduced or ended.',[
('Response maintenance','A learned response continues over time after relevant training conditions have changed or ended.'),('Maintenance probe','An assessment after training that checks whether the skill continues without assuming it does.')],
'Performance in a new setting addresses generalization; performance later addresses maintenance.',
'A person independently uses a trained budgeting skill three months after instruction ended. What does this most directly illustrate?',
['Response maintenance','Acquisition only','Stimulus discrimination only','A prompt hierarchy'],
'The key feature is continued performance after time has passed and training has ended.')
add('B.16','Motivating operations change both the effectiveness of a consequence and behavior previously related to that consequence.',[
('Establishing operation','Increases the effectiveness of a reinforcer and momentarily evokes related behavior.'),('Abolishing operation','Decreases the effectiveness of a reinforcer and momentarily abates related behavior.')],
'Identify both the value-altering and behavior-altering effects; do not infer an MO from a label alone.',
'After drinking enough water, a person temporarily finds water less reinforcing and makes fewer requests for it. Which relation is illustrated?',
['An abolishing operation for water','An establishing operation for water','A stimulus that always signals availability','Negative punishment'],
'The effectiveness of water and water-related requesting both decrease temporarily.')
add('B.17','Motivating operations and discriminative stimuli are antecedent variables with different functions.',[
('MO: value','Changes how effective a consequence is and momentarily changes related responding.'),('SD: availability','Signals that a particular response is more likely to contact reinforcement in that condition.')],
'Value and availability can both matter in the same example; identify the specific variable asked about.',
'A vending machine’s illuminated “available” sign indicates that a drink can be obtained by paying. Assuming thirst is unchanged, what function does the sign most directly serve?',
['A discriminative stimulus','An establishing operation for thirst','An unconditioned reinforcer','A punishment procedure'],
'The sign concerns the availability of reinforcement for paying, not primarily the value of the drink.')
add('B.18','Behavior may come under the influence of verbal descriptions of contingencies or be shaped through direct contact with consequences.',[
('Rule-governed behavior','Behavior influenced by a verbal description of a contingency.'),('Contingency-shaped behavior','Behavior acquired or changed through direct experience with environmental consequences.')],
'The two influences can coexist; distinguish the history described in the question.',
'A new employee follows a posted instruction to back up files before ever experiencing data loss or praise for doing so. What most directly describes this initial behavior?',
['Rule-governed behavior','Contingency-shaped behavior from personal data loss','Respondent extinction','Automatic punishment'],
'The initial behavior is influenced by a verbal rule rather than direct personal contact with the described outcome.')
add('B.19','Verbal operants are distinguished by controlling variables and consequences, not just the spoken word.',[
('Mand','A verbal response controlled by an MO and maintained by a characteristic consequence, such as a requested item or action.'),('Tact','A verbal response controlled by a nonverbal stimulus and typically maintained by generalized conditioned reinforcement.'),('Echoic and intraverbal','Echoic responding has point-to-point correspondence and formal similarity with a verbal model; intraverbal responding lacks point-to-point correspondence.')],
'The word “water” can be a mand, tact, or echoic under different controlling conditions.',
'A learner sees rain through a window, says “rain,” and receives conversational acknowledgment. Which verbal operant best fits the stated variables?',
['Tact','Mand for rain','Echoic','Textual response'],
'A nonverbal event, the visible rain, controls the response. No vocal model or request-producing consequence is described.')
add('B.20','More than one variable can control a verbal response, and one variable can contribute to several responses.',[
('Convergent multiple control','Several variables contribute to one response.'),('Divergent multiple control','One variable contributes to multiple responses.')],
'One response with several controlling variables is convergent control.',
'A thirsty learner sees a bottle and hears “What do you need?” before saying “water.” Multiple variables jointly influence the one response. What is illustrated?',
['Convergent multiple control','Divergent control only','Absence of stimulus control','Respondent extinction'],
'The scenario explicitly describes multiple sources of control converging on one verbal response.')
add('B.21','Some performances emerge without directly training every relation or response. Assessment must establish that the untrained performance actually occurs.',[
('Stimulus equivalence','A pattern including reflexivity, symmetry, and transitivity among related stimuli.'),('Generative performance','Novel responding that emerges from learned relations or repertoires without direct teaching of each instance.')],
'Do not call a relation emergent when that exact relation was directly taught.',
'After learning A→B and B→C relations, a learner demonstrates A→C without direct teaching. Which relation does this most directly illustrate?',
['Transitivity','Symmetry alone','Directly trained A→C responding','Extinction'],
'Transitivity concerns an untrained A→C relation following established A→B and B→C relations.')
add('B.22','Behavioral momentum theory distinguishes how fast behavior occurs from how persistent it is when conditions are disrupted.',[
('Response rate','How often responding occurs per unit time.'),('Resistance to change','Persistence of behavior when a disruptive change occurs; it is related to the reinforcement context.')],
'High response rate and high resistance to change are not the same measurement.',
'Two responses occur at similar rates. When a disruption is introduced, one persists much longer. Which dimension distinguishes them in a momentum analysis?',
['Resistance to change','Baseline rate alone','Response topography only','Latency by definition'],
'Persistence under disruption is resistance to change. Equal baseline rates do not imply equal persistence.')
add('B.23','The matching law describes a relation between relative responding and relative reinforcement across concurrent options.',[
('Relative response allocation','The proportion of total responding allocated to an option.'),('Basic matching relation','In the simple two-option form, B1/(B1+B2) is related to R1/(R1+R2), using obtained reinforcement rates.')],
'The model is a relation to evaluate, not a guarantee that every individual’s allocation exactly matches.',
'In a simplified matching example, option A supplies 30 obtained reinforcers and option B supplies 10. What share of responding would exact matching allocate to A?',
['75%','25%','30%','50%'],
'The relative reinforcement share is 30/(30+10)=0.75. Real behavior can deviate from exact matching.')
add('B.24','Imitation and observational learning involve models, but they are not identical.',[
('Imitation','A response resembles a model’s behavior and occurs under relevant control of that model.'),('Observational learning','Learning from observing others’ behavior and relevant consequences, without direct training of every response.')],
'Copying an action is not by itself proof of learning from the observed consequences.',
'After watching a coworker’s successful troubleshooting and its outcome, an employee later uses the solution on a new problem without direct instruction. Which broader process is illustrated?',
['Observational learning','Respondent extinction','Negative punishment','A permanent-product measure'],
'The employee learns by observing another person’s actions and outcomes rather than only immediately copying a movement.')

add('C.1','An operational definition makes the target behavior identifiable and measurable across observers.',[
('Observable definition','Describes actions or outcomes that can be detected, rather than inferred labels such as “unmotivated.”'),('Measurement boundaries','Specify onset, offset, inclusion criteria, and exclusions when needed to distinguish events consistently.')],
'A second observer should be able to use the definition without guessing what the writer intended.',
'Which definition is most operational?',
['A request is a spoken or device-generated “help” directed to the instructor','The learner has a bad attitude','The learner lacks motivation','The learner becomes frustrated'],
'The request definition specifies detectable behavior. The other choices are interpretive labels without measurement criteria.')
add('C.2','Measurement approaches differ in whether they directly sample behavior, rely on someone’s report, or inspect a lasting outcome.',[
('Direct versus indirect measurement','Direct measurement observes the target behavior; indirect measurement relies on reports, ratings, or recollections.'),('Permanent-product measurement','Measures an outcome left by behavior, when the product validly corresponds to the target activity.')],
'A product must be attributable to the behavior of interest; a finished worksheet does not prove who completed it.',
'An instructor counts correctly assembled units remaining after a work session, with conditions ensuring each unit was produced by the worker being assessed. Which measure is used?',
['Permanent product','Latency recording','Indirect interview only','Momentary time sampling'],
'The instructor measures a lasting result rather than observing each response as it occurs.')
add('C.3','Count, rate, and percentage answer different questions. Choose a denominator that makes observations comparable.',[
('Count and rate','Count is the number of responses. Rate is response count divided by observation time.'),('Percentage','A proportion multiplied by 100, such as correct responses divided by total opportunities.')],
'Compare rates, not raw counts, when observation durations differ.',
'A learner makes 18 responses in 30 minutes. What is the response rate per minute?',
['0.6 responses per minute','1.67 responses per minute','18 responses per minute','60 responses per minute'],
'Rate = 18 ÷ 30 = 0.6 responses per minute. Keep the time unit explicit.')
add('C.4','Temporal measures capture how long events last and how responses are spaced in time.',[
('Duration','Time from a behavior’s defined onset to its defined offset.'),('Latency','Time from a specified antecedent event to the beginning of a response.'),('Interresponse time','Time between defined points in consecutive responses, commonly the end of one and start of the next.')],
'For latency, identify the event that starts the clock.',
'An instruction is given, and the learner begins the requested task 35 seconds later. What does 35 seconds measure?',
['Latency','Duration of task performance','Response count','Percentage correct'],
'The interval begins with the instruction and ends when the response starts.')
add('C.5','Continuous measurement attempts to capture every relevant occurrence or temporal feature during observation. Discontinuous methods sample.',[
('Continuous measurement','Records all target events or relevant dimensions during the observation period.'),('Discontinuous measurement','Samples behavior at selected moments or within intervals rather than capturing every occurrence or dimension.')],
'A convenient sampling method is not automatically an accurate estimate for every purpose.',
'An observer records every occurrence and its exact onset and offset throughout a session. Which category best describes this?',
['Continuous measurement','Momentary time sampling','Partial-interval recording','Indirect measurement'],
'The observer attempts to capture all occurrences and their temporal features rather than sampling only intervals or moments.')
add('C.6','Discontinuous procedures impose different scoring rules and can introduce systematic estimation errors.',[
('Partial and whole interval','Partial interval scores occurrence at any point; whole interval scores occurrence throughout the entire interval.'),('Momentary time sampling','Record whether behavior is occurring at a specified instant, often at the end of each interval.')],
'Interval percentages are not interchangeable with event counts or exact percentage duration.',
'An observer checks only at the end of each 30-second interval and records whether the behavior is occurring at that instant. Which method is used?',
['Momentary time sampling','Whole-interval recording','Partial-interval recording','Continuous duration recording'],
'The observer scores one specified instant rather than any occurrence or continuous occurrence throughout the interval.')
add('C.7','Efficiency considers the outcomes achieved relative to time, effort, or other resources used.',[
('Trials to criterion','The number of teaching opportunities required to meet a defined performance criterion.'),('Resource-sensitive comparison','Compare equivalent outcomes alongside instructional time, cost, and other relevant inputs.')],
'An efficient intervention still needs meaningful, acceptable, and durable outcomes.',
'Two methods produce the same maintained skill level. One requires 20 teaching trials; the other requires 50. Which measure most directly captures the stated efficiency difference?',
['Trials to criterion','Response topography','Stimulus preference','Interobserver agreement'],
'The comparison concerns the teaching opportunities required to reach an equivalent criterion.')
add('C.8','A measurement system can be consistent yet fail to measure the intended behavior accurately or meaningfully.',[
('Validity','The extent to which measurement captures the intended behavior or dimension for its purpose.'),('Reliability and agreement','Reliability concerns consistency. Observer agreement compares records but does not alone establish accuracy.')],
'Two observers can agree and both be wrong.',
'Two observers consistently record identical values, but both use an incorrect event definition. What is the strongest conclusion?',
['High agreement does not establish valid or accurate measurement','Their agreement proves validity','The definition cannot affect measurement','Accuracy and agreement are identical'],
'Agreement is useful, but shared errors can produce agreement without valid or accurate measurement.')
add('C.9','Choose a measurement procedure based on the behavior’s dimensions, the decision to be made, and practical observation constraints.',[
('Dimension–procedure fit','Use a method that captures the aspect of behavior relevant to the goal.'),('Observation feasibility','Account for response frequency, duration, observer availability, and the setting without hiding limitations.')],
'Start with the question the data must answer, not the easiest recording form.',
'The goal is to reduce how long a recurring event lasts, and an observer can record exact start and stop times. Which primary measure fits best?',
['Duration','Preference ranking','Percentage of correct answers','A retrospective satisfaction rating'],
'The target dimension is time spent in each event, making duration the direct match.')
add('C.10','Graphs should make the relationship between time, conditions, and measured behavior clear without misleading scaling.',[
('Axes and units','Label time or sessions on the horizontal axis and the measured behavioral dimension with units on the vertical axis.'),('Condition changes','Mark meaningful phase changes and avoid implying continuity where observations or conditions do not support it.')],
'A graph is interpretable only when the reader knows what, when, and under which conditions data were recorded.',
'A line graph labels the vertical axis only “behavior.” What essential improvement is needed?',
['Identify the measured dimension and its units','Remove all axis labels','Replace observations with opinions','Hide phase changes'],
'The reader needs to know whether values represent counts, rates, duration, percentages, or another measure.')
add('C.11','Visual analysis examines patterns within phases and the relationship between patterns across conditions.',[
('Within-phase features','Level, trend, and variability describe the values and their pattern within a condition.'),('Between-phase features','Immediacy, overlap, and consistency across similar phases help evaluate effects of condition changes.')],
'A change in averages alone does not establish experimental control.',
'Scores begin low and increase steadily across baseline sessions. Which within-phase feature is most directly described?',
['Trend','Interobserver agreement','Response function','Procedural integrity'],
'Trend is the direction and rate of change across ordered observations within a phase.')
add('C.12','Procedural integrity measures how closely implementation matches the planned procedure.',[
('Integrity measure','Define observable implementation steps and record whether they are performed as specified.'),('Integrity percentage','One simple approach is correctly implemented opportunities divided by assessed opportunities, multiplied by 100.')],
'Low integrity can limit conclusions about an intervention’s effectiveness; outcome data alone do not show integrity.',
'An observer finds that 8 of 10 assessed intervention steps were implemented correctly. Using a simple step-based measure, what is integrity?',
['80%','8%','20%','125%'],
'The specified calculation is 8 ÷ 10 × 100 = 80%. Some procedures need more detailed or weighted measures.')

add('D.1','Experiments distinguish the manipulated variable from the behavior measured to evaluate its effect.',[
('Independent variable','The variable systematically manipulated, often an intervention or condition.'),('Dependent variable','The measured outcome expected to change as a function of the manipulation.')],
'The treatment is usually the IV; the recorded behavior is usually the DV.',
'A researcher introduces a prompting procedure and measures independently completed task steps. What is the dependent variable?',
['Independently completed task steps','The prompting procedure','The researcher’s credential','The room assignment unless manipulated'],
'Task completion is the measured outcome. The prompting procedure is the manipulated independent variable.')
add('D.2','A strong causal inference under the studied conditions is different from evidence that a finding extends beyond them.',[
('Internal validity','Confidence that the manipulated variable, rather than alternative explanations, accounts for observed change.'),('External validity','The extent to which findings generalize across relevant people, settings, behaviors, or times.')],
'Replication can strengthen generality; it does not excuse a weak causal demonstration in the original study.',
'An intervention has a convincing effect in one experiment, but it has not been evaluated in other settings. Which issue remains especially relevant?',
['External validity','Whether any behavior was measured at all','Whether an IV can exist','Whether graph axes are possible'],
'The open question is how far the result extends beyond the conditions directly studied.')
add('D.3','Alternative explanations can undermine causal conclusions even when behavior changes after intervention begins.',[
('History and maturation','Other events or changes over time may account for changes in the dependent variable.'),('Instrumentation and procedural confounds','Measurement changes or uncontrolled co-occurring interventions can create misleading apparent effects.')],
'Temporal sequence alone is not enough: “after” does not establish “because of.”',
'A new intervention begins on the same day the event definition is broadened. Recorded behavior increases. What threatens interpretation?',
['An instrumentation change','Perfect experimental control','A guaranteed treatment effect','Stimulus equivalence'],
'The measurement change could account for the apparent increase, confounding the intervention effect.')
add('D.4','Single-case experimental designs use repeated measurement and planned comparisons to evaluate effects for individual units.',[
('Repeated measurement','Observe the dependent variable across time under relevant conditions.'),('Prediction, verification, replication','Use design logic to predict behavior without the IV, evaluate that prediction, and reproduce an intervention effect.')],
'Single-case does not mean a single observation, and it does not always mean one participant.',
'A report includes one pretest and one posttest for one participant, with no repeated observations or planned replications. What is missing for a convincing single-case experiment?',
['Repeated measurement and experimental demonstrations','A participant’s name','A decorative graph','A longer title'],
'One pre/post comparison cannot supply the repeated measurement and replicated control required for a strong single-case causal demonstration.')
add('D.5','Single-case and group approaches answer related questions with different analytic emphases and design tradeoffs.',[
('Single-case emphasis','Evaluate functional relations and individual patterns through repeated within-unit comparisons.'),('Group-design emphasis','Compare groups under an allocation and analysis plan to estimate effects across sampled units.')],
'A group average may conceal individual differences; a single-case finding still needs generality evaluated.',
'A practitioner needs to see whether each individual’s behavior changes when an intervention is introduced at staggered times. Which approach directly fits that aim?',
['A single-case multiple-baseline approach','A satisfaction survey alone','One group mean without individual data','A retrospective anecdote'],
'The goal calls for repeated individual measurement and replicated, staggered demonstrations of an effect.')
add('D.6','Interpretation of single-case data depends on the design’s logic and the strength of repeated contrasts, not just visual improvement.',[
('Demonstration of effect','A pattern of changes linked convincingly to planned condition changes.'),('Competing explanations','Evaluate trends, variability, overlap, timing, and possible confounds before asserting control.')],
'Improvement can be clinically useful without constituting a strong experimental demonstration.',
'In a multiple-baseline graph, every tier improves before any intervention is introduced. What does this pattern imply?',
['It weakens attribution of improvement to the intervention','It proves experimental control','It makes baseline data irrelevant','It guarantees generalization'],
'Changes before intervention introduction do not follow the planned staggered logic and suggest alternative explanations.')
add('D.7','Select and identify single-case designs by their arrangement of conditions and their logic for demonstrating effects.',[
('Reversal and multiple baseline','Reversal changes conditions back and forth; multiple baseline staggers intervention across independent tiers.'),('Multielement and changing criterion','Multielement rapidly alternates conditions; changing criterion evaluates behavior against successive criterion changes.')],
'Reversal may be inappropriate when withdrawal poses risk or learned behavior is not reversible.',
'An intervention is introduced at different times across three independent routines while each routine is repeatedly measured. Which design is described?',
['Multiple baseline','A single uncontrolled pre/post comparison','Changing criterion','A concurrent-choice assessment'],
'The defining arrangement is staggered introduction across separate tiers.')
add('D.8','Different experimental analyses address which treatment works, which parts matter, and how much of a variable is needed.',[
('Comparative analysis','Compare two or more interventions or procedures.'),('Component analysis','Evaluate the contribution of individual elements of an intervention package.'),('Parametric analysis','Evaluate different values or amounts of an independent variable.')],
'Changing the amount of one variable is parametric; testing pieces of a package is component analysis.',
'A researcher compares 1-minute, 3-minute, and 5-minute values of the same procedure. What analysis is most directly described?',
['Parametric analysis','Component analysis','Stimulus preference ranking only','A records review'],
'The researcher systematically varies the value of one intervention parameter.')
add('D.9','Applying a design requires aligning the research question, behavior, measurement, experimental logic, and ethical constraints.',[
('Design feasibility','Consider whether behavior can reverse, tiers are sufficiently independent, and condition changes can be arranged.'),('Ethical design choice','Do not withdraw effective support or create risk simply to fit a preferred design.')],
'The strongest feasible ethical design is preferable to a design that is elegant but inappropriate.',
'An acquired safety skill is unlikely to disappear when training ends, and withdrawing protection would be inappropriate. Which design is worth considering instead of reversal?',
['A carefully planned multiple-baseline design','A mandatory reversal regardless of risk','No repeated measurement','A single testimonial'],
'Multiple-baseline logic can avoid requiring reversal, provided appropriate independent tiers and other design conditions are available.')

add('E.1','Ethical practice requires more than technical effectiveness. It integrates welfare, respect, honesty, and professional competence.',[
('Benefit and respect','Attend to the interests, dignity, rights, and preferences of people affected by services.'),('Integrity and competence','Represent work honestly, maintain professional skills, and operate within appropriate limits.')],
'An effective procedure is not automatically an ethically acceptable procedure.',
'A procedure improves a recorded outcome but ignores the client’s meaningful preferences and dignity. What is the strongest ethical response?',
['Reevaluate the procedure with welfare, rights, and preferences in view','Treat improved numbers as sufficient justification','Ignore all other stakeholders permanently','Assume consent is unnecessary'],
'Outcome improvement alone does not address the full ethical responsibilities of practice. Consult the current BACB Ethics Code for exact standards.')
add('E.2','Unethical behavior can harm clients, undermine trust, compromise records, and expose professionals to accountability processes.',[
('Direct and indirect harm','Harm can arise through unsafe practice, rights violations, inaccurate information, or disrupted services.'),('Prevention and response','Use sound supervision, documentation, consultation, and appropriate corrective action rather than concealment.')],
'Good intentions do not erase foreseeable risks or the need to correct errors.',
'An analyst discovers that service notes contain fabricated observations. What is the most appropriate direction?',
['Protect affected people and address the inaccurate records through proper procedures','Leave the records unchanged to avoid embarrassment','Use the invented data for treatment decisions','Create more fabricated entries to make the pattern consistent'],
'Fabrication compromises care and integrity. The specific corrective and reporting actions depend on applicable professional and legal requirements.')
add('E.3','Competence must match the specific service being provided and must be maintained as knowledge and circumstances change.',[
('Scope of competence','The areas in which a professional has the education, training, supervised experience, and skills needed to practice appropriately.'),('Maintaining competence','Seek relevant learning, supervision or consultation, and ongoing evaluation of performance.')],
'A credential alone does not establish competence in every population, procedure, or specialty.',
'A referral involves a specialized problem outside an analyst’s training. What is the best next step?',
['Evaluate competence and obtain appropriate support or referral before proceeding','Assume certification covers every specialty','Begin an unfamiliar procedure without support','Conceal the experience gap'],
'Recognizing limits and obtaining appropriate training, consultation, or referral protects service quality and clients.')
add('E.4','Confidential information should be accessed, stored, and disclosed only in ways consistent with authorization and applicable requirements.',[
('Confidentiality','Protect identifiable information and explain relevant limits of protection.'),('Necessary disclosure','When disclosure is authorized or required, limit it to information appropriate to the purpose and governing rules.')],
'Removing a name does not always make a case unidentifiable.',
'A public presentation removes a client’s name but includes enough unique details for local attendees to recognize the person. What is the concern?',
['The information may still be identifiable','No name always guarantees anonymity','Public presentations have no confidentiality duties','Only written records can be confidential'],
'Contextual details can permit identification. Use appropriate permission and privacy safeguards, and consult applicable requirements.')
add('E.5','Public statements should accurately describe qualifications, services, evidence, and professional relationships.',[
('Accurate representation','Do not misstate credentials, outcomes, endorsements, or the evidentiary basis of a service.'),('Responsible communication','Check marketing, social media, and third-party representations that fall within professional responsibilities.')],
'Anecdotes and testimonials are not substitutes for defensible outcome claims.',
'An advertisement promises that every client will achieve a specific outcome, although the provider cannot support that guarantee. What should change?',
['Remove the unsupported guarantee and communicate accurately','Keep it because marketing is exempt from ethics','Add more dramatic promises','Use a testimonial as proof of universal success'],
'Public claims must be defensible. A universal guarantee is not supported by isolated success stories.')
add('E.6','Ending services or supervision calls for appropriate planning, communication, documentation, and attention to continuity.',[
('Planned discontinuation','Define reasons and conditions for ending services and communicate them appropriately.'),('Transition support','Take relevant steps to transfer information, support continuity, and reduce avoidable disruption.')],
'Discontinuation is a process, not simply stopping appointments without communication.',
'A provider must leave a case. Which action best supports an ethical transition?',
['Communicate promptly and plan appropriate handoff and continuity','Stop attending without notice','Delete all records immediately','Promise permanent availability despite leaving'],
'A planned, documented transition reduces avoidable disruption while respecting consent, confidentiality, and applicable requirements.')
add('E.7','Multiple relationships can create conflicts, impair judgment, or increase the risk of exploitation.',[
('Multiple relationship','More than one kind of relationship with a person that may affect professional responsibilities.'),('Risk mitigation','Identify and address conflicts, establish boundaries, seek consultation, and document appropriate steps.')],
'Personal comfort with a relationship does not eliminate its professional risks.',
'A supervisee asks the supervisor to enter a substantial personal business partnership. What issue requires attention first?',
['Potential multiple-relationship conflicts and power imbalance','Whether the partnership sounds exciting','How to bypass supervision documentation','Whether expertise eliminates all risk'],
'An added financial relationship can affect objectivity and the supervisory power relationship. Assess and manage the conflict appropriately.')
add('E.8','Interpersonal skills support collaboration and ethical practice through clear communication, responsiveness, and respectful conflict resolution.',[
('Active listening','Attend to what another person says, clarify meaning, and check understanding rather than assuming.'),('Constructive feedback','Provide specific, respectful information that supports improvement and allows dialogue.')],
'Technical accuracy does not excuse communication that dismisses the person receiving services.',
'A caregiver disagrees with a proposed plan. Which response best demonstrates effective interpersonal skills?',
['Ask about the concerns, listen, and discuss workable changes','Repeat technical terms more loudly','Treat disagreement as proof of noncompliance','End all discussion immediately'],
'Listening and clarification can reveal goals, constraints, or misunderstandings that should inform collaboration.')
add('E.9','Cultural humility emphasizes ongoing self-reflection and learning rather than claiming complete knowledge of another person’s experience.',[
('Self-reflection','Examine one’s assumptions, limits, and position in professional relationships.'),('Collaborative learning','Invite people to describe their own values and experiences rather than treating group membership as a complete explanation.')],
'Ask and learn; do not presume that a cultural category determines an individual’s preferences.',
'An analyst notices an assumption about a family’s routine and asks the family how they understand and prioritize it. What is illustrated?',
['Cultural humility','A claim of complete cultural expertise','Ignoring culture','Automatic reinforcement'],
'The analyst questions an assumption and invites the family’s perspective rather than substituting a stereotype.')
add('E.10','Culturally responsive and inclusive practice adapts communication and service arrangements to meaningful individual and contextual variables.',[
('Cultural responsiveness','Use relevant knowledge of a person’s context, values, language, and preferences in planning and evaluation.'),('Inclusivity','Address barriers so people can participate meaningfully and access appropriate services.')],
'An identical format for everyone can still create unequal access.',
'A family cannot meaningfully participate in planning because materials are only in an unfamiliar language. Which adjustment is most directly responsive?',
['Provide appropriate language access and check understanding','Assume silence means agreement','Keep the format to treat everyone identically','Remove the family from planning'],
'Language access and checking understanding support informed participation. Use qualified resources when needed.')
add('E.11','Personal biases can influence what professionals notice, expect, recommend, and evaluate.',[
('Bias monitoring','Examine assumptions and patterns in decisions, not just intentions.'),('Bias mitigation','Use transparent criteria, seek relevant perspectives, review data, and change practices when inequities or errors are identified.')],
'Objectivity is a practice to maintain, not a personal quality to assume.',
'A supervisor consistently gives fewer challenging training opportunities to one group without performance-based reasons. What is an appropriate response?',
['Examine decision criteria and access patterns, then correct unjustified differences','Assume good intentions rule out bias','Preserve the pattern without review','Stop collecting relevant information'],
'Patterns in opportunity allocation warrant a review of bias and equitable, performance-relevant criteria.')
add('E.12','Professional certification is only one part of service-delivery eligibility and obligations.',[
('Certification and licensure','Certification and governmental authorization are distinct; requirements depend on jurisdiction and role.'),('Service requirements','Check applicable laws, organizational requirements, funding rules, and professional obligations before delivering services.')],
'Do not assume one jurisdiction’s requirements apply everywhere. Verify current rules from the relevant authority.',
'A certified practitioner plans to offer services in a different jurisdiction. What should be checked before beginning?',
['Applicable authorization and service-delivery requirements in that jurisdiction','Only whether the credential is printed correctly','Nothing beyond certification','Whether another practitioner once worked there'],
'Jurisdiction-specific requirements must be verified. This scenario does not provide legal advice or a current licensing determination.')

add('F.1','Records can provide relevant history and context, but they need to be evaluated for relevance, accuracy, and limits.',[
('Records review','Examine appropriate educational, medical, service, and assessment information within consent and authorization boundaries.'),('Corroboration','Distinguish historical reports from current direct evidence and resolve important discrepancies.')],
'An old record may guide questions without establishing the current function of behavior.',
'A five-year-old report assigns a behavior’s function. The current context is very different. How should the report be used?',
['As historical information to inform current assessment','As permanent proof of current function','As a substitute for all present data','As information to publish publicly'],
'Historical information is useful context, but current assessment is needed to evaluate present behavior and conditions.')
add('F.2','Cultural variables can affect the meaning, acceptability, implementation, and impact of assessment and intervention.',[
('Relevant context','Identify individual values, language, routines, and community factors that matter for the assessment question.'),('Individualized inquiry','Ask stakeholders rather than assigning preferences based on group membership.')],
'Cultural relevance is determined with the person and stakeholders, not inferred from stereotypes.',
'A skill assessment assumes that all families use the same meal routine. What is an appropriate improvement?',
['Ask about the family’s actual routines and adapt assessment relevance','Score unfamiliar routines as deficits automatically','Ignore family input','Assume every member of a cultural group has identical practices'],
'Assessment should distinguish lack of relevant experience from a meaningful skill need and consider the person’s context.')
add('F.3','A useful assessment identifies existing capabilities as well as areas where new skills or support would matter.',[
('Skill strengths','Demonstrated abilities that can support goals, participation, and further learning.'),('Needs assessment','Identify meaningful gaps relative to the person’s goals, context, and opportunities, not just a test score.')],
'A low score does not automatically identify the most important intervention priority.',
'A learner has strong device-based communication but little spoken language. What should a strengths-based assessment do?',
['Recognize existing communication and evaluate meaningful support needs','Treat all communication as absent','Ignore the learner’s preferred method','Select goals solely from a single total score'],
'Existing functional skills should inform planning, alongside the person’s preferences and meaningful areas of need.')
add('F.4','Preference assessments identify relative selection or engagement. Reinforcer assessments evaluate whether a consequence increases behavior.',[
('Preference assessment','Systematically evaluate choices or engagement with potential items or activities.'),('Reinforcer assessment','Test whether contingent access actually increases a target response.')],
'A preferred item is a candidate reinforcer, not proof of a reinforcing effect.',
'A person repeatedly selects one activity over others. What conclusion is justified from preference data alone?',
['The activity is a potential reinforcer worth evaluating','The activity will reinforce every response','The activity is an unconditioned reinforcer','No further evaluation is ever useful'],
'Selection indicates relative preference. Reinforcing effectiveness must be demonstrated for the relevant behavior and conditions.')
add('F.5','Descriptive assessment records naturally occurring relations among antecedents, behavior, and consequences without the experimental manipulation required for a functional analysis.',[
('ABC observation','Document events before behavior, the behavior itself, and events following it.'),('Descriptive inference','Use observed patterns to develop hypotheses while recognizing that correlation does not establish function.')],
'The most common consequence after behavior is not automatically the maintaining reinforcer.',
'Attention often follows a target behavior in classroom observations. What is the strongest conclusion from these data alone?',
['Attention is associated with the behavior and may warrant further assessment','Attention has been proven to maintain the behavior','No other function is possible','An experimental functional relation has already been demonstrated'],
'Naturally occurring associations support hypotheses but can reflect confounds or coincidental patterns.')
add('F.6','Functional analysis tests hypotheses about behavioral function through planned manipulation and comparison of conditions.',[
('Experimental test','Systematically vary relevant environmental variables and measure resulting behavior.'),('Risk-sensitive assessment','Use appropriate expertise, consent, safeguards, and individualized procedures; assessment must not create avoidable risk.')],
'An FA is not just an ABC chart. This study note is not a protocol for conducting one.',
'A qualified team systematically compares carefully designed test and control conditions to evaluate a suspected maintaining consequence. What distinguishes this from descriptive assessment?',
['Experimental manipulation of relevant variables','A longer interview form','Use of a behavior label','The presence of any graph'],
'The defining distinction is the systematic manipulation and comparison used to test a functional hypothesis.')
add('F.7','Determining service needs includes asking whether behavior-analytic support is appropriate and whether other professionals or resources are needed.',[
('Appropriateness of services','Match the person’s goals and assessed needs to available competent services.'),('Referral and collaboration','Seek relevant medical, psychological, educational, or other input when needs exceed scope or suggest additional causes.')],
'Behavioral assessment does not replace evaluation of possible medical concerns.',
'A person shows a sudden unexplained change in behavior accompanied by signs of physical discomfort. What is the best next direction?',
['Seek appropriate medical evaluation while coordinating relevant support','Assume a behavioral function without considering health','Implement an unfamiliar intervention immediately','Ignore the change until it is convenient'],
'Abrupt changes with possible discomfort warrant appropriate medical attention and coordinated assessment rather than a premature behavioral explanation.')
add('F.8','Social significance concerns whether goals, procedures, and outcomes matter to the person and relevant stakeholders.',[
('Social validity','Evaluate the importance of goals, acceptability of procedures, and value of outcomes.'),('Person-centered priorities','Emphasize meaningful participation, autonomy, safety, and quality of life rather than convenience alone.')],
'Difference from a social norm is not, by itself, a sufficient reason to target a behavior.',
'A harmless personal habit is targeted only because it looks unusual, despite the person’s objections. What should be reconsidered?',
['The goal’s social significance, acceptability, and respect for autonomy','Only the recording form','Whether unusual behavior is always a deficit','How to avoid hearing the person’s preferences'],
'Goals require meaningful justification with attention to the person’s welfare, rights, and preferences.')

add('G.1','A reinforcement procedure arranges a consequence contingent on behavior and evaluates whether the desired behavior actually increases.',[
('Contingent reinforcement','Deliver the relevant consequence in relation to the defined response, according to the plan.'),('Evaluate the effect','Measure future behavior rather than assuming an item, praise, or relief is reinforcing.')],
'Calling a consequence a reward does not establish its behavioral function.',
'An instructor offers praise after task completion, but completion does not increase. What can be concluded?',
['A reinforcing effect has not been demonstrated by these data','Praise is always positive reinforcement','The procedure must be negative punishment','Measurement is unnecessary'],
'Reinforcement is identified by an increase in future behavior; intention and stimulus type are not sufficient.')
add('G.2','Differential reinforcement makes reinforcement depend on a specified response pattern rather than treating all responding the same.',[
('DRA and DRI','Reinforce an alternative response; DRI specifies an alternative that cannot occur simultaneously with the target response.'),('DRO and DRL','DRO depends on absence of the target response during a specified period; DRL reinforces a lower rate that meets a criterion.')],
'DRO does not specify a particular replacement skill; DRA does.',
'A learner is taught to request assistance with a device, and those requests receive help as an alternative to an existing problem response. Which procedure is most directly described?',
['Differential reinforcement of alternative behavior','Differential reinforcement of other behavior only','Response cost','A fixed-time schedule'],
'Reinforcement is arranged for a specified alternative response. Functional and ethical details still require individualized planning.')
add('G.3','Time-based schedules deliver a stimulus based on elapsed time rather than making each delivery contingent on a target response.',[
('Fixed-time schedule','Deliver the stimulus after a constant time interval, independent of the target response.'),('Variable-time schedule','Deliver after varying intervals around an average, independent of the target response.')],
'Fixed time is not fixed interval: fixed interval requires a qualifying response.',
'An event is delivered every five minutes regardless of whether a specified response occurs. Which schedule is described?',
['Fixed time','Fixed interval','Fixed ratio','Variable ratio'],
'Delivery is time-based and response-independent, with a constant interval.')
add('G.4','Conditioned reinforcers acquire effectiveness through learning and should be evaluated rather than presumed effective.',[
('Establishing conditioned value','Arrange appropriate associations with established reinforcement according to a coherent learning plan.'),('Token systems','Tokens can acquire reinforcing effects through reliable exchange for meaningful backup reinforcers.')],
'A token with no effective learning or exchange history may not function as a reinforcer.',
'A new point system awards symbols, but participants do not know what the points mean or how to use them. What should be evaluated first?',
['Whether the points have acquired reinforcing value and a clear exchange relation','Whether points are automatically unconditioned reinforcers','Whether more decorative symbols solve every problem','Whether outcomes can be ignored'],
'The system depends on learned effectiveness and meaningful, reliable contingencies, not simply displaying points.')
add('G.5','Effective teaching considers whether the consequence currently matters and whether the learner can identify when a response will produce it.',[
('MO considerations','Assess momentary variables affecting the consequence’s value and related responding.'),('SD arrangements','Make relevant reinforcement-availability conditions clear and support transfer to appropriate cues.')],
'Consider value and discriminative control without creating unnecessary deprivation or distress.',
'A training plan checks both whether an activity is currently valued and whether the cue clearly signals access for the target response. Which two variables are being considered?',
['Motivating operations and discriminative stimuli','Only punishment magnitude','Only response duration','Observer agreement and graph color'],
'The plan addresses reinforcer effectiveness and the antecedent signaling its availability.')
add('G.6','Discrimination procedures teach which response is appropriate under particular stimulus conditions.',[
('Simple discrimination','A response is differentially reinforced in the presence of particular antecedent stimuli.'),('Conditional discrimination','The function of one stimulus depends on another stimulus or contextual condition.')],
'In a conditional discrimination, the correct choice depends on another relevant cue.',
'A learner selects a red card when hearing “red” and a blue card when hearing “blue,” with both cards available on every trial. Which arrangement is illustrated?',
['Conditional discrimination','Unsignaled extinction','A fixed-time schedule','Response maintenance only'],
'The auditory sample changes which comparison card is correct; the relevant relation is conditional.')
add('G.7','Prompts provide supplementary assistance for a response. Their use should support learning and eventual independence.',[
('Response prompts','Supplementary cues or assistance directed at the response, such as a model or an appropriate verbal cue.'),('Stimulus prompts','Changes to task stimuli that make relevant features more salient.')],
'A plan should address how control will transfer from prompts to the appropriate natural stimuli.',
'A matching task temporarily enlarges the distinguishing feature of the correct comparison stimulus. Which type of prompt is most directly described?',
['Stimulus prompt','Response cost','Negative punishment','A verbal response model'],
'The task stimulus itself is altered to highlight a relevant feature.')
add('G.8','Prompt fading reduces supplementary assistance while evaluating transfer to the appropriate cues.',[
('Prompt fading','Systematically reduce prompt intensity, intrusiveness, or other features according to performance.'),('Time delay','Change the interval between the relevant instruction or cue and the supplementary prompt.')],
'Reducing help is useful only when performance and independence are monitored.',
'An instructor gradually increases the wait between a task cue and a supplementary model, giving the learner a chance to respond independently. What procedure is highlighted?',
['Time delay','Response cost','A preference assessment','Whole-interval recording'],
'The temporal gap before the prompt is adjusted to support independent responding under the original cue.')
add('G.9','Models demonstrate a response for the learner. Evaluate whether observing the model produces the intended learning.',[
('Live modeling','A person demonstrates the target behavior directly.'),('Video modeling','A recorded model demonstrates the target behavior; assess performance rather than assuming viewing equals learning.')],
'Modeling is an instructional arrangement; imitation is the learner’s corresponding response.',
'A learner watches a recorded demonstration of a work routine and then practices it. What instructional procedure is used?',
['Video modeling','A token exchange alone','Negative punishment','A permanent-product definition'],
'The recorded demonstration is the defining feature. Practice and feedback may be additional components.')
add('G.10','Instructions and rules can guide behavior when they are understandable, relevant, and supported by the context.',[
('Effective instruction','Specify the action clearly in language and a format the learner can use.'),('Rule evaluation','Check comprehension and observed performance rather than equating exposure to a rule with mastery.')],
'Failure to follow a rule may reflect unclear instructions, missing skills, or competing conditions.',
'A worker receives a long, unfamiliar verbal instruction and cannot perform the task. What is a useful next step?',
['Check comprehension and prerequisite skills, then clarify instruction','Assume intentional defiance','Repeat the exact wording indefinitely','Remove all feedback permanently'],
'Instruction should fit the learner’s repertoire and the task. Assessment helps identify the actual barrier.')
add('G.11','Shaping builds a response by reinforcing successive approximations rather than requiring the final form immediately.',[
('Successive approximations','Intermediate response forms that progressively resemble the target dimension or performance.'),('Criterion shifts','Change the reinforcement requirement gradually based on observed responding.')],
'Shaping changes a response dimension; chaining links separate steps.',
'A trainer first reinforces a rough approximation of a new hand movement, then progressively requires closer versions of the final movement. Which procedure is described?',
['Shaping','Backward chaining','Momentary time sampling','Response cost'],
'Reinforcement is differentially arranged for increasingly accurate approximations of one target movement.')
add('G.12','Task analysis identifies component steps. Chaining teaches the connected sequence.',[
('Task analysis','Break a meaningful multistep skill into teachable and assessable components.'),('Forward, backward, and total-task teaching','Teach from the beginning, from the end, or provide practice across the entire sequence with needed assistance.')],
'Choosing a chaining method depends on the learner, task, and assessment; no single method is always best.',
'An instructor completes earlier steps while the learner initially performs the last step, then gradually transfers earlier steps to the learner. Which arrangement is described?',
['Backward chaining','Forward chaining','Shaping a single movement only','A multiple schedule'],
'Teaching starts with the terminal step and progressively includes earlier steps in the chain.')
add('G.13','Teaching opportunities may be organized as discrete trials or as ongoing access to response opportunities.',[
('Trial-based procedures','Use defined opportunities with a beginning, a response opportunity, and a consequence or feedback.'),('Free-operant procedures','Allow repeated responding without a separate instructor-defined trial for each response.')],
'The distinction is how opportunities are arranged, not whether teaching is individualized.',
'A learner can repeatedly practice a skill during an activity without waiting for a new instruction before each response. Which arrangement is most consistent?',
['Free-operant procedure','A required discrete trial for every response','Respondent extinction','A changing-criterion graph'],
'The learner has ongoing response opportunities rather than distinct instructor-initiated trials for each response.')
add('G.14','Group contingencies differ in whose performance determines access to consequences and who receives them.',[
('Independent and dependent','Independent arrangements depend on each person’s own performance; dependent arrangements make a group outcome depend on selected member performance.'),('Interdependent','A shared outcome depends on the combined or specified performance of multiple group members.')],
'Evaluate fairness, coercion, peer pressure, and individual access before using group contingencies.',
'Each employee earns an incentive solely by meeting their own criterion, regardless of coworkers’ performance. Which group arrangement is illustrated?',
['Independent group contingency','Dependent group contingency','Interdependent group contingency','A chained schedule'],
'Each individual’s consequence depends on that individual’s performance rather than selected members or combined group performance.')
add('G.15','Generalization should be planned and measured instead of left to chance.',[
('Multiple exemplars','Teach across relevant variations in stimuli, people, settings, or responses.'),('Natural contingencies','Connect new skills to reinforcement and cues available in the environments where they should be used.')],
'A skill demonstrated only with one instructor and one material has not yet shown broad generalization.',
'A learner practices requesting directions with several people in several realistic settings. Which aim is most directly supported?',
['Stimulus generalization across relevant conditions','Eliminating all natural cues','Restricting the skill to one trainer','Respondent extinction'],
'Practice across varied relevant conditions can support transfer, which should still be directly assessed.')
add('G.16','Maintenance planning considers how useful behavior will continue after intensive teaching or support is reduced.',[
('Natural reinforcement','Help the behavior contact consequences available in everyday settings.'),('Follow-up and schedule changes','Evaluate continued performance as support changes and use appropriate follow-up checks.')],
'Maintenance is an outcome to verify, not a promise created by ending intervention.',
'A skill performs well only when a trainer delivers frequent special rewards. Which maintenance concern is most relevant?',
['Whether the skill will contact effective consequences in ordinary settings','Whether the data sheet has enough colors','Whether a successful teaching session proves lifelong use','Whether all reinforcement should be stopped abruptly'],
'Transition to sustainable conditions should be planned and evaluated rather than assuming a trained response will persist automatically.')
add('G.17','Punishment procedures require careful ethical and functional evaluation, safeguards, and ongoing assessment of effects and risks.',[
('Positive and negative punishment','Add a stimulus or remove one after behavior, with a demonstrated decrease in future behavior.'),('Safeguards and alternatives','Prioritize appropriate reinforcement-based approaches and assess rights, consent, risks, and applicable professional requirements.')],
'This is exam-level classification, not authorization to implement a punishment procedure.',
'A proposed procedure reduces a response but also creates avoidable distress and suppresses useful communication. What should the team do?',
['Reassess risks, alternatives, and the person’s welfare rather than relying on reduction alone','Continue solely because the target rate decreased','Ignore communication changes','Treat distress as proof of success'],
'Behavior reduction does not by itself justify a procedure. Ethical evaluation includes unwanted effects, alternatives, rights, and meaningful outcomes.')
add('G.18','Interventions can affect behavior and experience beyond the selected target. Monitor these effects deliberately.',[
('Collateral effects','Changes in other useful or problematic behavior that occur alongside the intended change.'),('Emotional or elicited effects','Relevant distress, avoidance, or other responses that may occur during intervention and warrant evaluation.')],
'An outcome graph for one target can miss important harm or loss of participation.',
'Target behavior decreases, but the person increasingly avoids the service setting. Which action is most appropriate?',
['Assess the avoidance and intervention acceptability as potential unwanted effects','Ignore avoidance because it is not the target','Declare complete success immediately','Remove all stakeholder feedback'],
'Evaluation should include collateral effects and the person’s experience, not only the selected target measure.')
add('G.19','Instruction can establish relations that support new, untrained performance. Tests must distinguish genuine emergence from directly taught responses.',[
('Derived relations','Relations demonstrated without direct training of every relation, given an appropriate learning history.'),('Generative teaching','Design instruction and probes to evaluate meaningful novel responding beyond trained examples.')],
'Test untrained relations without accidentally teaching the answer during the probe.',
'After a relational teaching program, an instructor probes a novel relation without prompts or teaching feedback. What is the purpose?',
['Evaluate whether the untrained relation emerges','Directly teach the exact relation during the probe','Measure only procedural duration','Prove all future relations will emerge'],
'A probe can assess emergent performance when it does not itself supply direct training of the tested answer.')

add('H.1','Intervention goals should state what the person will do, in what conditions, and how success will be measured.',[
('Observable target','Specify detectable behavior instead of a broad evaluative label.'),('Criterion and context','State relevant conditions, measurement dimensions, performance criteria, and time or consistency requirements.')],
'Measurable is not enough: the goal must also be meaningful and appropriate.',
'Which goal is most measurable?',
['During five scheduled opportunities, independently request needed assistance on at least four across three sessions','Be more confident','Behave appropriately at all times','Have a better attitude'],
'The first goal identifies behavior, opportunities, a criterion, and a consistency requirement.')
add('H.2','Intervention selection combines assessment evidence with goals, preferences, resources, and the provider’s competence.',[
('Assessment–intervention fit','Use the assessed function, skill needs, and context to justify the selected approach.'),('Feasibility and acceptability','Consider stakeholder capacity, burden, preference, and the quality of supporting evidence.')],
'A popular intervention is not automatically the right intervention for this person.',
'Two evidence-supported options fit the assessed need, but one cannot be implemented reliably in the person’s daily setting. What should inform selection?',
['Feasibility, acceptability, and expected meaningful benefit alongside evidence','Popularity alone','Which name sounds most technical','The assumption that implementation does not matter'],
'Intervention selection needs a workable fit with the person, setting, assessment, and available resources.')
add('H.3','Alternative behaviors should be meaningful, efficient, and compatible with the person’s communication methods and environment.',[
('Functionally relevant alternative','A response that can access an appropriate outcome related to the assessed need.'),('Social validity and effort','Consider autonomy, preferences, response effort, and whether the alternative can work in daily life.')],
'A replacement that is much harder or ineffective may not compete successfully.',
'A proposed alternative request requires a long sequence that the learner cannot perform, while a simple accessible communication option is available. Which issue deserves attention?',
['Response effort and accessibility of the alternative','Only the appearance of the communication method','Whether harder always means better','Whether functional outcomes are irrelevant'],
'An effective alternative should be accessible and able to produce meaningful outcomes with reasonable effort.')
add('H.4','Anticipating unwanted effects helps teams plan safeguards, monitoring, and criteria for modifying a procedure.',[
('Risk planning','Identify foreseeable problems, who may be affected, and how to reduce and detect harm.'),('Adjustment criteria','Specify when data, safety, acceptability, or changing needs require reassessment.')],
'A plan should explain what to do when implementation produces problems, not only when it works.',
'A team writes an intervention plan without any procedure for responding to foreseeable unwanted effects. What is missing?',
['A risk-mitigation and monitoring plan','A more impressive title','A guarantee of success','A reason to stop collecting outcome data'],
'Planning should include prevention, monitoring, and appropriate responses to foreseeable adverse or unwanted effects.')
add('H.5','Behavior can return when reinforcement conditions or contexts change. Relapse concepts help explain and plan for these possibilities.',[
('Resurgence','A previously reduced response returns when reinforcement for an alternative response worsens or stops.'),('Renewal','A previously reduced response returns after a change in context from the one in which reduction occurred.')],
'Relapse is a reason to evaluate conditions and support, not to blame the learner.',
'An old response returns after a previously reinforced alternative no longer produces its outcome. Which relapse pattern is most directly described?',
['Resurgence','Stimulus equivalence','Fixed-interval scalloping','Generalized imitation'],
'The described trigger is worsening reinforcement for the alternative response, a defining feature of resurgence.')
add('H.6','Integrity data help determine whether the planned intervention was actually implemented and what support implementers need.',[
('Assess implementation','Measure critical steps and conditions instead of assuming the written plan was followed.'),('Respond to low integrity','Identify barriers such as unclear instructions, missing skills, resources, or consequences and provide appropriate support.')],
'Poor outcomes with low integrity do not provide a clean test of the planned intervention.',
'Outcome data show little improvement, and observers find that critical intervention steps were rarely implemented. What should happen before declaring the plan ineffective?',
['Address implementation barriers and evaluate delivery','Assume the plan was fully tested','Blame the learner','Discard integrity data'],
'When the procedure was not implemented adequately, its intended effects have not received a fair evaluation.')
add('H.7','Data-based intervention decisions examine meaningful outcomes, implementation quality, acceptability, and risks over time.',[
('Effectiveness review','Compare data to goals and inspect patterns instead of relying on impressions alone.'),('Modification decisions','Adjust, continue, fade, or discontinue based on the combined evidence and the person’s needs.')],
'One favorable data point is not enough to establish stable, meaningful benefit.',
'A plan is implemented reliably but produces no meaningful improvement across an adequate evaluation, and stakeholders report excessive burden. What is appropriate?',
['Reassess and modify or replace the plan using the evidence','Continue indefinitely without review','Ignore stakeholder feedback','Change the graph scale to appear successful'],
'Consistently poor outcomes and burden warrant a reasoned reassessment rather than cosmetic reporting or indefinite continuation.')
add('H.8','Collaboration coordinates perspectives and expertise while maintaining clear roles, consent, and accountability.',[
('Interprofessional collaboration','Work with relevant professionals and stakeholders within each person’s scope and responsibilities.'),('Shared goals and communication','Agree on meaningful objectives, exchange authorized information, and resolve conflicts constructively.')],
'Collaboration does not mean claiming competence outside one’s discipline.',
'A client’s goals involve communication access and medical concerns as well as behavioral learning. What approach best supports services?',
['Coordinate with appropriate professionals and the client around shared goals','Make all decisions alone outside scope','Ignore other disciplines by default','Share all records publicly to save time'],
'Coordinated, authorized collaboration can address needs that cross professional boundaries while preserving roles and privacy.')

add('I.1','Behavior-analytic supervision uses observable goals, active teaching, feedback, and data to support competent and ethical practice.',[
('Skill development','Build and evaluate the supervisee’s performance rather than merely discussing cases.'),('Client protection','Connect supervision to service quality, ethical decisions, and the welfare of people receiving services.')],
'Supervision hours alone do not prove competence.',
'A supervisor tracks observed skills and provides targeted practice and feedback rather than only signing time logs. What benefit is most directly supported?',
['Demonstrable supervisee competence and service quality','Guaranteed exam success','Elimination of all professional responsibility','A substitute for client consent'],
'Performance-focused supervision can support competence and quality; attendance documentation alone cannot demonstrate these outcomes.')
add('I.2','Effective supervisory relationships require clear expectations, communication, appropriate boundaries, and a workable plan for feedback and evaluation.',[
('Defined expectations','Clarify responsibilities, goals, evaluation methods, logistics, and applicable agreements.'),('Feedback relationship','Create opportunities to ask questions, report concerns, receive feedback, and address disagreements appropriately.')],
'Ambiguous expectations can undermine evaluation even when both people have good intentions.',
'A supervisee is unsure what will be observed and how performance will be evaluated. What should the supervisor establish?',
['Clear goals, criteria, roles, and feedback procedures','Surprise criteria revealed only after failure','Only an informal promise that things will work out','A ban on questions'],
'Transparent expectations and evaluation procedures support a fair and productive relationship.')
add('I.3','Equitable supervision considers access, context, and fair opportunities to learn and demonstrate competence.',[
('Equitable access','Address unnecessary barriers to training, feedback, resources, and meaningful opportunities.'),('Fair evaluation','Use relevant, transparent criteria and examine bias or contextual factors that may distort evaluation.')],
'Equity does not require lowering essential competence standards; it requires fair access and defensible assessment.',
'A required training opportunity is consistently offered in a format one supervisee cannot access, although an equivalent accessible format exists. What should change?',
['Provide equitable access while preserving the essential competency objective','Treat inaccessible delivery as a competency deficit','Remove all competency standards','Assume identical format is always fair'],
'The learning objective can remain while unnecessary access barriers are addressed.')
add('I.4','Supervision goals should follow an assessment of current skills and the demands of the supervisee’s work.',[
('Baseline performance','Observe existing skills and identify strengths and specific gaps.'),('Observable supervision goal','State the performance, conditions, and criteria that will demonstrate progress or mastery.')],
'A vague goal such as “be more professional” needs observable criteria.',
'A supervisee needs to improve feedback delivery. Which goal is more useful?',
['During observed role-plays, give specific behavior-based feedback meeting the agreed checklist criterion','Understand feedback better','Try harder in meetings','Become excellent eventually'],
'The selected goal specifies observable performance and a criterion that can guide teaching and evaluation.')
add('I.5','Performance management applies behavioral principles to staff or supervisee performance with clear goals and supportive conditions.',[
('Behavioral skills training','Combine instruction, modeling, rehearsal, and feedback, with performance evaluated against a criterion.'),('Performance supports','Ensure expectations, materials, feedback, and appropriate consequences support the target work behavior.')],
'Explaining a procedure is only one part of skills training; the learner needs to perform it.',
'After describing and demonstrating a skill, a supervisor asks the trainee to practice and provides specific feedback. What package is illustrated?',
['Behavioral skills training','An interview-only assessment','Response cost','A simple written rule without practice'],
'Instruction, modeling, rehearsal, and feedback form the commonly taught BST sequence.')
add('I.6','A function-based approach asks what conditions support or interfere with supervisee performance rather than assuming a personal flaw.',[
('Performance assessment','Check whether expectations, skills, resources, opportunities, and consequences support the required behavior.'),('Matched support','Select training or environmental changes that address the identified barrier.')],
'A skill deficit and a resource barrier require different solutions.',
'A trained employee misses a documentation deadline because the required system is unavailable during the assigned work period. What intervention best matches the identified barrier?',
['Fix access or scheduling so the task can be performed','Repeat skills training as the only response','Assume laziness without assessment','Set a deadline that is even less feasible'],
'The described problem is an opportunity or resource barrier, not necessarily missing skill.')
add('I.7','Supervisory practices should be evaluated by their effects on supervisee performance and relevant service outcomes.',[
('Supervision outcome data','Track changes in observed skills, implementation, and relevant client outcomes while respecting confidentiality.'),('Data-based adjustment','Modify supervisory methods when performance, feedback, or context indicates they are not working adequately.')],
'Satisfaction with supervision is useful feedback, but it is not a substitute for performance evidence.',
'Supervisees report enjoying meetings, but observed implementation has not improved. What should the supervisor do?',
['Review performance data and adjust supervisory teaching and supports','Treat positive satisfaction ratings as sufficient proof of effectiveness','Stop observing performance','Guarantee future improvement without changes'],
'Evaluation should include demonstrated skill and service quality alongside satisfaction and other relevant feedback.')

missing=[t['id'] for t in outline['topics'] if t['id'] not in NOTES]
assert not missing,missing
assert len(NOTES)==104
course={
 'id':'bcba-6','title':'6th Edition BCBA Outline','subtitle':'Behavior analysis · Independent study pack',
 'description':'104 topics across Domains A–I. Learn a concept, recall it, then apply it.',
 'provenance':'Topic IDs, titles, order, and AllDayABA links come from the user-supplied index. The linked article bodies were not retrieved. All notes, definitions, flashcards, and hypothetical scenarios are original supplemental study content, not extracted AllDayABA text or official BACB exam items. This pack has not been independently reviewed for clinical or examination completeness.',
 'sourceFile':'Pasted markdown(20260927-152039).md',
 'domains':outline['domains'],'topics':[]
}
for pos,t in enumerate(outline['topics']):
    n=NOTES[t['id']]
    cards=[{'id':f"{t['id']}-c{i+1}",'question':f"What is meant by {c['term'].lower()}?",'answer':c['definition']} for i,c in enumerate(n['concepts'])]
    # Deterministic rotation prevents a fixed answer position without hidden randomness.
    sc=n['scenario']; offset=(pos*3+1)%4
    opts=sc['options']; rotated=opts[offset:]+opts[:offset]
    sc={**sc,'id':f"{t['id']}-s1",'options':rotated,'correctIndex':(4-offset)%4}
    course['topics'].append({**t,**n,'cards':cards,'scenario':sc,'origin':'original-supplement'})
# An actually usable second curriculum for testing the selector and adding personal material.
custom={'id':'my-material','title':'My study material','subtitle':'Your own notes, cards, and scenarios',
 'description':'Create a topic or import a JSON study pack. Nothing is sent to a server.',
 'provenance':'User-authored material. Accuracy and permissions are the responsibility of its author.',
 'domains':[{'id':'1','title':'My topics'}],'topics':[]}
pack={'schemaVersion':1,'courses':[course,custom]}
(ROOT/'src/content.json').write_text(json.dumps(pack,ensure_ascii=False,indent=2))
print('Created',len(course['topics']),'topics,',sum(len(t['cards']) for t in course['topics']),'cards,',len(course['topics']),'scenarios')
