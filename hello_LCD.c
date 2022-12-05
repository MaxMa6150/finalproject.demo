/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include "pico/stdlib.h"
#include "ws2812.h"

#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "hardware/clocks.h"
#include "ws2812.pio.h"
#include "LCD_st7735.h"

// #define IS_RGBW true
// #define NUM_PIXELS 150

// #ifdef PICO_DEFAULT_WS2812_PIN
// #define WS2812_PIN PICO_DEFAULT_WS2812_PIN
// #else
// // default to pin 2 if the board doesn't have a default WS2812 pin defined
// #define WS2812_PIN 12
// #define WS2812_POWER_PIN 11
// #endif

void game_init(){
    stdio_init_all();
     ST7735_Init();
     ST7735_DrawImage(0, 0, 80, 160, arducam_logo);
     sleep_ms(1000);
     ST7735_FillScreen(ST7735_GREEN);
     ST7735_WriteString(5, 20, "Launchpad", Font_11x18, ST7735_BLACK, ST7735_GREEN);
     ST7735_WriteString(5, 60, "Music game", Font_11x18, ST7735_BLACK, ST7735_GREEN);
     sleep_ms(1000);
}

int count_score(int time, int score){
    ST7735_FillScreen(ST7735_GREEN);
    if (time <= 250){
        ST7735_WriteString(5, 20, "EXCELLENT!", Font_11x18, ST7735_BLACK, ST7735_GREEN);
        ST7735_WriteString(25, 60, "+2", Font_11x18, ST7735_BLACK, ST7735_GREEN);
        score += 2;
    }
    else if (time <= 500){
        ST7735_WriteString(5, 20, "Good!", Font_11x18, ST7735_BLACK, ST7735_GREEN);
        ST7735_WriteString(25, 60, "+1", Font_11x18, ST7735_BLACK, ST7735_GREEN);
        score += 1;
    }
    else{
        ST7735_WriteString(5, 20, "Oops!", Font_11x18, ST7735_BLACK, ST7735_GREEN);
        ST7735_WriteString(25, 60, "+0", Font_11x18, ST7735_BLACK, ST7735_GREEN);
    }
    return score;
}

void score_summary(int score){
    ST7735_FillScreen(ST7735_GREEN);
    char str_score[20];
     sprintf(str_score, "%d", score);
     ST7735_WriteString(5, 20, "Total:", Font_11x18, ST7735_BLACK, ST7735_GREEN);
     ST7735_WriteString(30, 60, str_score, Font_11x18, ST7735_BLACK, ST7735_GREEN);
}

int main() {
     game_init();
     int score = 0;
     for(int i  = 0; i <= 6; i++){
        int r = rand() % 750;
        score = count_score(r, score);
        sleep_ms(2000);
     }
     score_summary(score);
     
    return 0;
}
