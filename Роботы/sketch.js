function setup()
{
	//create a canvas for the robot
	createCanvas(1000, 700);
}

function draw()
{
	strokeWeight(2);

	//robot body 1 
	fill(238, 130, 238);
	rect(90, 200, 120, 110);
	rect(70, 200, 30, 85);
	rect(200, 200, 30, 85);
    fill(123, 104, 238)
    rect(90, 200, 25, 85); 
    rect(183, 200, 25, 85);
    rect(90, 220, 120, 90);
    rect(105, 310, 35, 30);
	rect(160, 310, 35, 30);
  
    fill(240, 230, 140)
	rect(105, 320, 35, 20);
	rect(160, 320, 35, 20);

	//robot body 2 
  fill(102, 205, 170);
  rect(370, 200, 120, 110);
  rect(340, 200, 30, 100);
  rect(490, 200, 30, 100);
  rect(400, 330, 30, 30);
  rect(430, 330, 30, 30);

  fill(0);
  rect(370, 200, 120, 110);
  rect(340, 200, 30, 90);
  rect(490, 200, 30, 90);
  rect(400, 310, 30, 30);
  rect(430, 310, 30, 30);
  fill(128, 0, 0);
  rect(425, 200, 15, 40);
  fill(255, 255, 255)
  triangle(430, 245, 405, 170, 475, 170);
  fill(128, 0, 0);
  rect(425, 200, 15, 40);
  fill(139, 69, 19);
  rect(400, 340, 30, 20);
  rect(430, 340, 30, 20);


	


	// !!! Draw the robot heads - You shouldn't need to change this code !!!

	//robot head 1
	fill(238, 130, 238);
	rect(100, 110, 100, 90, 10);
    //robot head 2
	fill(102, 205, 170);
    rect(380, 100, 100, 100, 10);
    102
    fill(0)
    rect(380, 9, 100, 100, 10);
    rect(370, 102, 120, 10, 10)

	//ears
	fill(148, 0, 211);

	//robot ears 1
	rect(93, 130, 10, 33);
	rect(197, 130, 10, 33);

	//robot ears 2
    fill(0, 128, 128);
	rect(370, 130, 10, 33);
	rect(480, 130, 10, 33);




	//robots' antennas
	fill(250, 250, 0);
    // robot antenna 1.1
	ellipse(130, 93, 10, 10);
   // robot antenna 1.1
	ellipse(130, 83, 10, 10);
  // robot antenna 1.2
	ellipse(170, 93, 10, 10);
   // robot antenna 1.2
	ellipse(170, 83, 10, 10);
    
    //robots' antennas
	fill(200, 0, 200);
    // robot antenna 1.1
	rect(120, 98, 20, 10);
   // robot antenna 1.2
    rect(160, 98, 20, 10);
   


	//robot 1's eyes
	fill(255);
	ellipse(125, 130, 26, 26);
	point(125, 130);
	ellipse(175, 130, 26, 26);
	point(175, 130);

	//robot 2's eyes
	ellipse(415, 130, 26, 26);
  point(415, 130);
  ellipse(455, 130, 26, 26);
  point(455, 130);


	//robots' noses
	fill(186, 85, 211);
    //robot 1 nose
	triangle(150, 135, 135, 160, 165, 160);
    //robot 2 nose
	fill(0, 128, 128);
    triangle(435, 125, 425, 165, 445, 160);
	

	//robot 1 mouth
	noFill();
	beginShape();
	vertex(128, 175);
	vertex(136, 185);
	vertex(142, 175);
	vertex(150, 185);
	vertex(158, 175);
	vertex(166, 185);
	vertex(174, 175);
	endShape();

	//robot 2 mouth
	beginShape();
	vertex(428, 175);
	vertex(436, 185);
	vertex(442, 175);
	vertex(450, 185);
	vertex(458, 175);
	vertex(466, 185);
	vertex(474, 175);
	endShape();

	
}