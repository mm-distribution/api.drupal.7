# HtaccessTest::assertFileAccess()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3387–3391 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3387-L3391)
- **Class:** [HtaccessTest](../HtaccessTest.md)
- **Module/theme:** system

## Signature

```php
protected function assertFileAccess($path, $response_code)
```

## Documentation

```text
Asserts that a file exists and requesting it returns a specific response.

@param string $path
  Path to file. Without leading slash.
@param int $response_code
  The expected response code. For example: 200, 403 or 404.
```

## Code

```php
  protected function assertFileAccess($path, $response_code) {
    $this->assertTrue(file_exists(drupal_realpath($path)), format_string('@filename exists.', array('@filename' => $path)));
    $this->drupalGet(file_create_url($path), array('external' => TRUE));
    $this->assertResponse($response_code, "Response code to $path should be $response_code");
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
