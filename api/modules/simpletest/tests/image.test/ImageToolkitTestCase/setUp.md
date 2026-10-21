# ImageToolkitTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/image.test`](../_file.md), lines 16–41 · [local source](../../../../../../source/modules/simpletest/tests/image.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test#L16-L41)
- **Class:** [ImageToolkitTestCase](../ImageToolkitTestCase.md)
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
    $modules = func_get_args();
    if (isset($modules[0]) && is_array($modules[0])) {
      $modules = $modules[0];
    }
    $modules[] = 'image_test';

    parent::setUp($modules);

    // Use the image_test.module's test toolkit.
    $this->toolkit = 'test';

    // Pick a file for testing.
    $file = current($this->drupalGetTestFiles('image'));
    $this->file = $file->uri;

    // Setup a dummy image to work with, this replicate image_load() so we
    // can avoid calling it.
    $this->image = new stdClass();
    $this->image->source = $this->file;
    $this->image->info = image_get_info($this->file);
    $this->image->toolkit = $this->toolkit;

    // Clear out any hook calls.
    image_test_reset();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/image.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/image.test) · Licensed GPL-2.0-or-later (see LICENSE)._
