# DrupalGotoTest::testDrupalGetDestination()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1504–1515 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1504-L1515)
- **Class:** [DrupalGotoTest](../DrupalGotoTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalGetDestination()
```

## Documentation

```text
Test drupal_get_destination().
```

## Code

```php
  function testDrupalGetDestination() {
    $query = $this->randomName(10);

    // Verify that a 'destination' query string is used as destination.
    $this->drupalGet('common-test/destination', array('query' => array('destination' => $query)));
    $this->assertText('The destination: ' . $query, 'The given query string destination is determined as destination.');

    // Verify that the current path is used as destination.
    $this->drupalGet('common-test/destination', array('query' => array($query => NULL)));
    $url = 'common-test/destination?' . $query;
    $this->assertText('The destination: ' . $url, 'The current path is determined as destination.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
