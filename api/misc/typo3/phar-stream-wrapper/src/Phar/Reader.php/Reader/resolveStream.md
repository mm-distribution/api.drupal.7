# Reader::resolveStream()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 145–153 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L145-L153)
- **Class:** [Reader](../Reader.md)

## Signature

```php
private function resolveStream()
```

## Documentation

```text
Resolves stream in order to handle compressed Phar archives.

@return string
```

## Code

```php
    private function resolveStream()
    {
        if ($this->fileType === 'application/x-gzip' || $this->fileType === 'application/gzip') {
            return 'compress.zlib://';
        } elseif ($this->fileType === 'application/x-bzip2') {
            return 'compress.bzip2://';
        }
        return '';
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
