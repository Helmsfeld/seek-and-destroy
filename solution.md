# The solution

It might seem impossible first, but actually - it is. We proceed in
a divide-and-conquer manner and tackle the problem in four steps:

0. Find a strategy for velocity 0
1. Find a strategy for velocity 1
2. Generalize for arbitrary velocities
3. Combine all the strategies into one

## A strategy for velocity 0

> tl;dr
> Shoot at 0, -1, 1, -2, 2

Velocity 0 means that the spaceship doesn't move. So it sits at z=1000, or z=-412
or z=591423212343234. To simplify the situation 
even further, let's assume that it sits at a position z>=0. A simple
strategy that will finally hit it is to shoot consecutively at z=0, z=1,
z=3 and so on. With every shot the distance between the spaceships position
and our shot decreases by 1 - mission accomplished.

However, what if the spaceship sits on some point z<0? If we know that fact
we can simply shoot at z=-1, z=-2, z=-3 and so on - mission accomplished.

So we have now two strategies, one for the case where the spaceship sits at
z>=0, the other for the case that it sits on the negative side.
Since we don't know which is the case, we must make sure that each strategy
gets its fair share and is eventually executed step by step. In the case of
two strategies, let's execute first strategy one, then two, then one again,
then two. And so on. So we'll shoot at z=0, -1, 1, -2, 2, -3, 3, ...and will
eventually hit the ship.

The two key observations here, that will lead us to solve the whole puzzle, are
1. Given a certain special case, 
   we found a systematic way to decrease the distance between the ship and
   our shots one by one. To concentrate on the distance and how to decrease it
   systematically is key because that way we don't need to know what the
   initial distance actually is.
2. If we have different strategies, we can execute them turn by turn.
   This will get more complicated with the other strategies, especially
   since there will be infinitely many ones. But the basic idea is the same:
   interleave the strategies in a systematic way.

## A strategy for velocity 1

Case z>0. Again, let's simplify and first assume that the spaceship starts at
a position on the positive side, say z=100. Then the next problem is, that we didn't
state yet what *exactly* we mean by velocity 1: We didn't talk of the
direction. So let's be precise and say that velocity 1 means that the 
ship flies in positive direction and let's denote velocity -1 to express
that the ship flies towards negative infinity.

So let's more precise and consider:

Case z>=0, velocity 1.
In our example the spaceship travels from 100 to 101 to 102 and so on.
Let's shoot first (when the spaceship is at 100) shoot at 0 so that the 
distance between our shot and the ship is 100. In the next step, the ship
is at 101. Now, where must we shoot so that the distance is now 99, one less
than our initial distance? We must of course shoot at z=2. If we follow the
pattern and do the math, we must shoot consecutively at 0, 2, 4, 6 and so on.

If we replace the concrete initial position 100 with a variable, we can easily
verify that the same sequence of shots works always for velocity 1:

The ship travels from initial position z>0 to z+1 then z+2, z+3, .... or even
more general: at time t the ship is at position z+t. If we shoot at time t
at position 2t, the distance between our shot and the spaceship turns out
to be z+t - 2t = z-t. Which means nothing less than we'll hit the spaceship
at time t=z.

It takes maybe a few concrete examples to actually feel that shooting
only at every second position will do the job. But once you're there, the
generalization to arbitrary velocities will be straight forward.

Before that, we need to consider the remaining cases.

Case z>=0, velocity -1.

Just shoot at 0 all the time. The spaceship flies towards 0 from z to z-1
z-2, etc. Finally we'll hit it.

Case z<0, velocity 1.

This case is symmetric to the previous case. Only this time the ship
flies from the left side towards 0. So always shoot at 0.

Case z<0, velocity -1. Again symmetry helps us and we can deduce from the
case z>=0, velocity 1 that we must shoot at z=0, -2, -4, -6, or more generally
at z=-2t.

Before we turn to the matter of interleaving all the strategies, we turn
now to arbitrary velocities.

## Arbitrary velocities.



