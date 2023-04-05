package com.blind75.arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class BestTimeToBuyFinderTest {

  @DisplayName("The highest profit of 5 should be returned")
  @Test
  void maxProfit1() {
    int[] prices = new int[]{7, 1, 5, 3, 6, 4};
    int bestDayToSell = new BestTimeToBuyFinder().maxProfit(prices);
    assertEquals(5, bestDayToSell);
  }

  @DisplayName("The highest profit of 0 should be returned")
  @Test
  void maxProfit2() {
    int[] prices = new int[]{7, 6, 4, 3, 1};
    int bestDayToSell = new BestTimeToBuyFinder().maxProfit(prices);
    assertEquals(0, bestDayToSell);
  }
}