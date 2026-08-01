#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <stdio.h>

void show_boot_splash(SDL_Renderer* renderer, SDL_Texture* texture);

int main(int argc, char *argv[])
{
  printf("Troposphere boot splash app thing");
  if (argc < 2){
    printf("Add path to Boot splash png");
    return 1;
  }

  const char* image_path = argv[1];
  
  if (SDL_Init(SDL_INIT_VIDEO) < 0){

    fprintf(stderr, "SDL_Init error %s\n", SDL_GetError());

    return 1;
  }

  if (!IMG_Init(IMG_INIT_PNG) && IMG_INIT_PNG){

      fprintf(stderr,"SDL IMG_INIT_PNG Failed to ... well init", IMG_GetError);

      SDL_Quit();
      return 1;
  }


  SDL_Window* AppWindow = SDL_CreateWindow("Fullscreen Test", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,0,0,SDL_WINDOW_FULLSCREEN_DESKTOP | SDL_WINDOW_SHOWN);


  if (!AppWindow){
    fprintf(stderr,"App window init Crashed %s\n", SDL_GetError());
    IMG_Quit();
    SDL_Quit();
    
  }


  SDL_ShowCursor(SDL_DISABLE);

  SDL_Renderer* renderer = SDL_CreateRenderer(AppWindow,-1,SDL_RENDERER_ACCELERATED);

  SDL_Texture* BootSplash_Texture = IMG_LoadTexture(renderer, image_path);

  if(!BootSplash_Texture){
    fprintf(stderr, "Failed to load texture %s\n", IMG_GetError());
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(AppWindow);

    IMG_Quit();
    SDL_Quit();
    return 1;
  }

  int running = 1 ;
  SDL_Event event;



  while (running) {

    while(SDL_PollEvent(&event)){
      if (event.type == SDL_QUIT){
        running =0;
      } else if (event.type == SDL_KEYDOWN){
        if (event.key.keysym.sym == SDLK_ESCAPE ||event.key.keysym.sym == SDLK_q ){
          running =0;
        }
      }
    }


    SDL_SetRenderDrawColor(renderer, 0,0,0,255);
    SDL_RenderClear(renderer);

    show_boot_splash(renderer, BootSplash_Texture);
    SDL_RenderPresent(renderer);

     









  }


    SDL_DestroyTexture(BootSplash_Texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(AppWindow);
    IMG_Quit();
    SDL_Quit();

  return EXIT_SUCCESS;
}


void show_boot_splash( SDL_Renderer* renderer , SDL_Texture* texture){

  if (!texture){

    SDL_SetRenderDrawColor(renderer, 0,50,0,50);
    SDL_RenderClear(renderer);

  } else {

    SDL_RenderCopy(renderer, texture, NULL,NULL);

  }


 SDL_RenderCopy(renderer,texture, NULL, NULL);

}
