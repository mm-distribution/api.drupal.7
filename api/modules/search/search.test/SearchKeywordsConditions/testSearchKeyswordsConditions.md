# SearchKeywordsConditions::testSearchKeyswordsConditions()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1246–1267 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1246-L1267)
- **Class:** [SearchKeywordsConditions](../SearchKeywordsConditions.md)
- **Module/theme:** search

## Signature

```php
function testSearchKeyswordsConditions()
```

## Documentation

```text
Verify the kewords are captured and conditions respected.
```

## Code

```php
  function testSearchKeyswordsConditions() {
    // No keys, not conditions - no results.
    $this->drupalGet('search/dummy_path');
    $this->assertNoText('Dummy search snippet to display');
    // With keys - get results.
    $keys = 'bike shed ' . $this->randomName();
    $this->drupalGet("search/dummy_path/{$keys}");
    $this->assertText("Dummy search snippet to display. Keywords: {$keys}");
    $keys = 'blue drop ' . $this->randomName();
    $this->drupalGet("search/dummy_path", array('query' => array('keys' => $keys)));
    $this->assertText("Dummy search snippet to display. Keywords: {$keys}");
    // Add some conditions and keys.
    $keys = 'moving drop ' . $this->randomName();
    $this->drupalGet("search/dummy_path/bike", array('query' => array('search_conditions' => $keys)));
    $this->assertText("Dummy search snippet to display.");
    $this->assertRaw(print_r(array('search_conditions' => $keys), TRUE));
    // Add some conditions and no keys.
    $keys = 'drop kick ' . $this->randomName();
    $this->drupalGet("search/dummy_path", array('query' => array('search_conditions' => $keys)));
    $this->assertText("Dummy search snippet to display.");
    $this->assertRaw(print_r(array('search_conditions' => $keys), TRUE));
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
