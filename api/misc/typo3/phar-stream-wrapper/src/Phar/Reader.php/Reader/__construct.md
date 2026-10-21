# Reader::__construct()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 34–45 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L34-L45)
- **Class:** [Reader](../Reader.md)

## Signature

```php
public function __construct($fileName)
```

## Documentation

```text
@param string $fileName
```

## Code

```php
    public function __construct($fileName)
    {
        if (strpos($fileName, '://') !== false) {
            throw new ReaderException(
                'File name must not contain stream prefix',
                1539623708
            );
        }

        $this->fileName = $fileName;
        $this->fileType = $this->determineFileType();
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
