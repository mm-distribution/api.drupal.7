# HtaccessTest::testFileAccess()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3372–3377 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3372-L3377)
- **Class:** [HtaccessTest](../HtaccessTest.md)
- **Module/theme:** system

## Signature

```php
function testFileAccess()
```

## Documentation

```text
Iterates over protected files and calls assertNoFileAccess().
```

## Code

```php
  function testFileAccess() {
    foreach ($this->getProtectedFiles() as $file => $response_code) {
      file_put_contents($file, '# test content');
      $this->assertFileAccess($file, $response_code);
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
