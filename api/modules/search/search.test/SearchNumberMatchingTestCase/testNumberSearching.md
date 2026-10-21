# SearchNumberMatchingTestCase::testNumberSearching()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1412–1438 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1412-L1438)
- **Class:** [SearchNumberMatchingTestCase](../SearchNumberMatchingTestCase.md)
- **Module/theme:** search

## Signature

```php
function testNumberSearching()
```

## Documentation

```text
Tests that all the numbers can be searched.
```

## Code

```php
  function testNumberSearching() {
    for ($i = 0; $i < count($this->numbers); $i++) {
      $node = $this->nodes[$i];

      // Verify that the node title does not appear on the search page
      // with a dummy search.
      $this->drupalPost('search/node',
        array('keys' => 'foo'),
        t('Search'));
      $this->assertNoText($node->title, format_string('%number: node title not shown in dummy search', array('%number' => $i)));

      // Now verify that we can find node i by searching for any of the
      // numbers.
      for ($j = 0; $j < count($this->numbers); $j++) {
        $number = $this->numbers[$j];
        // If the number is negative, remove the - sign, because - indicates
        // "not keyword" when searching.
        $number = ltrim($number, '-');

        $this->drupalPost('search/node',
          array('keys' => $number),
          t('Search'));
        $this->assertText($node->title, format_string('%i: node title shown (search found the node) in search for number %number', array('%i' => $i, '%number' => $number)));
      }
    }

  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
