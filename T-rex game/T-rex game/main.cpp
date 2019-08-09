#include <SFML/Graphics.hpp>
using namespace sf;

#define WIDTH 600
#define HEIGHT 300

struct Position
{
	int x;
	int y;
};

int main(void)
{
	RenderWindow window(VideoMode(WIDTH, HEIGHT), "Dinosaur Game. By DongYoung");
	window.setFramerateLimit(60);

	//dino
	Texture t1;
	Texture t2;
	t1.loadFromFile("images/GreatTH.png");
	t2.loadFromFile("images/GreatTH.png");

	Sprite dinoArr[2];
	dinoArr[0] = Sprite(t1);
	dinoArr[1] = Sprite(t2);

	static const int DINO_Y_BOTTOM = HEIGHT - t1.getSize().y;
	Position dinoPos;
	dinoPos.x = 50;
	dinoPos.y = DINO_Y_BOTTOM;

	int index = 0;
	float frame = 0.f;
	float frameSpeed = 0.6f;
	const int changeCount = 5;

	const int gravity = 4;
	bool isJumping = false;
	bool isBottom = true;

	//obstacle
	Texture t3;
	t3.loadFromFile("images/TH.png");
	Sprite block(t3);

	static const int BLOCK_Y_BOTTOM = HEIGHT - t3.getSize().y;
	Position blockPos;
	blockPos.x = WIDTH - 20;
	blockPos.y = BLOCK_Y_BOTTOM;

	const int blockSpeed = 3;

	while (window.isOpen())
	{
		Event e;
		while (window.pollEvent(e))
		{
			if (e.type == Event::Closed)
			{
				window.close();
			}
		}
		//logic.

		//dino jump.
		if (Keyboard::isKeyPressed(Keyboard::Space))
		{
			if (isBottom && !isJumping)
			{
				//make jumping stage;
				isJumping = true;
				isBottom = false;
			}
		}

		//dino jump(up and down)
		if (isJumping)
		{
			dinoPos.y -= gravity;
		}
		else
		{
			dinoPos.y += gravity;
		}

		//dino jump limit, dino bottom limit.
		if (dinoPos.y >= DINO_Y_BOTTOM)
		{
			dinoPos.y = DINO_Y_BOTTOM;
			isBottom = true;
		}
		if (dinoPos.y <= DINO_Y_BOTTOM - 140)
		{
			isJumping = false;
		}

		//dino step.
		frame += frameSpeed;
		if (frame > changeCount)
		{
			frame -= changeCount;
			++index;
			if (index >= 2) { index = 0; }
		}

		//obstacle move.
		if (blockPos.x <= 0)
		{
			blockPos.x = WIDTH;
		}
		else
		{
			blockPos.x -= blockSpeed;
		}

		//obstacle Position.
		block.setPosition(blockPos.x, blockPos.y);

		//dino Position.
		dinoArr[index].setPosition(dinoPos.x, dinoPos.y);

		//draw.
		window.clear(Color::White);
		window.draw(dinoArr[index]);
		window.draw(block);
		window.display();
	}

	return 0;
}