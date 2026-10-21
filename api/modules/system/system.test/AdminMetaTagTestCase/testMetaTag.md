# AdminMetaTagTestCase::testMetaTag()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1038–1043 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1038-L1043)
- **Class:** [AdminMetaTagTestCase](../AdminMetaTagTestCase.md)
- **Module/theme:** system

## Signature

```php
public function testMetaTag()
```

## Documentation

```text
Verify that the meta tag HTML is generated correctly.
```

## Code

```php
  public function testMetaTag() {
    list($version, ) = explode('.', VERSION);
    $string = '<meta name="Generator" content="Drupal ' . $version . ' (http://drupal.org)" />';
    $this->drupalGet('node');
    $this->assertRaw($string, 'Fingerprinting meta tag generated correctly.', 'System');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
