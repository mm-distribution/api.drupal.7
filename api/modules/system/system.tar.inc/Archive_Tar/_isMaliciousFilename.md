# Archive_Tar::_isMaliciousFilename()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1870–1879 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1870-L1879)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
private function _isMaliciousFilename($file)
```

## Documentation

```text
Detect and report a malicious file name

@param string $file

@return bool
```

## Code

```php
    private function _isMaliciousFilename($file)
    {
        if (strpos($file, '://') !== false) {
            return true;
        }
        if (strpos($file, '../') !== false || strpos($file, '..\\') !== false) {
            return true;
        }
        return false;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
