package com.blind75.arrays;

public class BestTimeToBuyFinder {

    public int maxProfit(int[] prices) {
        int bestDayToBuy = 0;
        int bestDayToSell = 0;
        int bestProfit = 0;
        while (bestDayToSell < prices.length) {
            if (prices[bestDayToSell] > prices[bestDayToBuy]) {
                int profit = prices[bestDayToSell] - prices[bestDayToBuy];
                bestProfit = Math.max(profit, bestProfit);
            } else {
                bestDayToBuy = bestDayToSell;
            }
            bestDayToSell++;
        }
        return bestProfit;
    }

}
