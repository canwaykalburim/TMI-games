using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ItemButton : MonoBehaviour {

    public Text itemDisplayer;

    public string itemName;

    public int level;

    [HideInInspector]

    public int currentCost;
    public int startCurrentCost = 1;

    [HideInInspector]

    public int goldPerSec;
    public int startGoldPerSec = 1;

    public float upgradePow = 5.25f;
    public float costsPow = 0.25f;

    [HideInInspector]

    public bool isPurchased = false;

    void Start()
    {
        DataController.GetInstance().LoadItemButton(this);
        StartCoroutine("AddGoldLoop");

        UpdateUI();
    }

    public void PurchaseItem()
    {
        if (DataController.GetInstance().GetGold() >= currentCost)
        {
            isPurchased = true;
            DataController.GetInstance().SubGold(currentCost);
            level++;

            UpdateItem();
            UpdateUI();

            DataController.GetInstance().SaveItemButton(this);
        }
    }

    IEnumerator AddGoldLoop()
    {
        while (true)
        {
            if (isPurchased)
            {
                DataController.GetInstance().AddGold(goldPerSec);
            }
            yield return new WaitForSeconds(1.0f);
        }
    }

    public void UpdateItem()
    {
        goldPerSec += startGoldPerSec * (int) Mathf.Pow(upgradePow, level);
        currentCost = startCurrentCost * (int)Mathf.Pow(costsPow, level);
    }

    public void UpdateUI()
    {
        itemDisplayer.text = itemName + "\nLevel: " + level + "\nCost: " + currentCost + 
            "\nGold Per Sec: " + goldPerSec + "\nIs Purchased: " + isPurchased;
    }
}
