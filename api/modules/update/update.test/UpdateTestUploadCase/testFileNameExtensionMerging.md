# UpdateTestUploadCase::testFileNameExtensionMerging()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 746–752 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L746-L752)
- **Class:** [UpdateTestUploadCase](../UpdateTestUploadCase.md)
- **Module/theme:** update

## Signature

```php
function testFileNameExtensionMerging()
```

## Documentation

```text
Ensures that archiver extensions are properly merged in the UI.
```

## Code

```php
  function testFileNameExtensionMerging() {
    $this->drupalGet('admin/modules/install');
    // Make sure the bogus extension supported by update_test.module is there.
    $this->assertPattern('/file extensions are supported:.*update-test-extension/', "Found 'update-test-extension' extension");
    // Make sure it didn't clobber the first option from core.
    $this->assertPattern('/file extensions are supported:.*tar/', "Found 'tar' extension");
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
