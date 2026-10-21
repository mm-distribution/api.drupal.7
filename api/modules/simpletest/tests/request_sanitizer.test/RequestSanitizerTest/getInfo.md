# RequestSanitizerTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/request_sanitizer.test`](../_file.md), lines 23–29 · [local source](../../../../../../source/modules/simpletest/tests/request_sanitizer.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test#L23-L29)
- **Class:** [RequestSanitizerTest](../RequestSanitizerTest.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'DrupalRequestSanitizer',
      'description' => 'Test the DrupalRequestSanitizer class',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/request_sanitizer.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/request_sanitizer.test) · Licensed GPL-2.0-or-later (see LICENSE)._
