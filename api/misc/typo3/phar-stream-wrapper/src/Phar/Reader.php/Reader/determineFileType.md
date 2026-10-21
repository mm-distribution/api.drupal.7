# Reader::determineFileType()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 158–165 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L158-L165)
- **Class:** [Reader](../Reader.md)

## Signature

```php
private function determineFileType()
```

## Documentation

```text
@return string
```

## Code

```php
    private function determineFileType()
    {
        if (class_exists('\\finfo')) {
            $fileInfo = new \finfo();
            return $fileInfo->file($this->fileName, FILEINFO_MIME_TYPE);
        }
        return $this->determineFileTypeByHeader();
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
