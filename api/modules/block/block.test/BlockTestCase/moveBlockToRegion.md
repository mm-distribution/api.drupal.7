# BlockTestCase::moveBlockToRegion()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 338–357 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L338-L357)
- **Class:** [BlockTestCase](../BlockTestCase.md)
- **Module/theme:** block

## Signature

```php
function moveBlockToRegion($block, $region)
```

## Documentation

_No docblock in source._

## Code

```php
  function moveBlockToRegion($block, $region) {
    // Set the created block to a specific region.
    $edit = array();
    $edit['blocks[' . $block['module'] . '_' . $block['delta'] . '][region]'] = $region;
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    // Confirm that the block was moved to the proper region.
    $this->assertText(t('The block settings have been updated.'), format_string('Block successfully moved to %region_name region.', array( '%region_name' => $region)));

    // Confirm that the block is being displayed.
    $this->drupalGet('node');
    $this->assertText(t($block['title']), 'Block successfully being displayed on the page.');

    // Confirm that the custom block was found at the proper region.
    $xpath = $this->buildXPathQuery('//div[@class=:region-class]//div[@id=:block-id]/*', array(
      ':region-class' => 'region region-' . str_replace('_', '-', $region),
      ':block-id' => 'block-' . $block['module'] . '-' . $block['delta'],
    ));
    $this->assertFieldByXPath($xpath, NULL, format_string('Custom block found in %region_name region.', array('%region_name' => $region)));
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
