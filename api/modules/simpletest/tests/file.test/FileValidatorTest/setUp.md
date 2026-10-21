# FileValidatorTest::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 377–387 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L377-L387)
- **Class:** [FileValidatorTest](../FileValidatorTest.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();

    $this->image = new stdClass();
    $this->image->uri = 'misc/druplicon.png';
    $this->image->filename = drupal_basename($this->image->uri);

    $this->non_image = new stdClass();
    $this->non_image->uri = 'misc/jquery.js';
    $this->non_image->filename = drupal_basename($this->non_image->uri);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
