# FileTestCase::createDirectory()

- **Type:** Method
- **File:** [`modules/simpletest/tests/file.test`](../_file.md), lines 176–183 · [local source](../../../../../../source/modules/simpletest/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test#L176-L183)
- **Class:** [FileTestCase](../FileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function createDirectory($path = NULL)
```

## Documentation

```text
Create a directory and assert it exists.

@param $path
  Optional string with a directory path. If none is provided, a random
  name in the site's files directory will be used.
@return
  The path to the directory.
```

## Code

```php
  function createDirectory($path = NULL) {
    // A directory to operate on.
    if (!isset($path)) {
      $path = file_default_scheme() . '://' . $this->randomName();
    }
    $this->assertTrue(drupal_mkdir($path) && is_dir($path), 'Directory was created successfully.');
    return $path;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
