# Reader::determineFileTypeByHeader()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 173–191 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L173-L191)
- **Class:** [Reader](../Reader.md)

## Signature

```php
private function determineFileTypeByHeader()
```

## Documentation

```text
In case ext-fileinfo is not present only the relevant types
'application/x-gzip' and 'application/x-bzip2' are resolved.

@return string
```

## Code

```php
    private function determineFileTypeByHeader()
    {
        $resource = fopen($this->fileName, 'r');
        if (!is_resource($resource)) {
            throw new ReaderException(
                sprintf('Resource %s could not be opened', $this->fileName),
                1557753055
            );
        }
        $header = fgets($resource, 4);
        fclose($resource);
        $mimeType = '';
        if (strpos($header, "\x42\x5a\x68") === 0) {
            $mimeType = 'application/x-bzip2';
        } elseif (strpos($header, "\x1f\x8b") === 0) {
            $mimeType = 'application/x-gzip';
        }
        return $mimeType;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
