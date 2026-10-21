# Reader::resolveFourByteLittleEndian()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 210–228 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L210-L228)
- **Class:** [Reader](../Reader.md)

## Signature

```php
public static function resolveFourByteLittleEndian($content, $start)
```

## Documentation

```text
@param string $content
@param int $start
@return int
```

## Code

```php
    public static function resolveFourByteLittleEndian($content, $start)
    {
        $payload = substr($content, $start, 4);
        if (!is_string($payload)) {
            throw new ReaderException(
                sprintf('Cannot resolve value at offset %d', $start),
                1539614260
            );
        }

        $value = unpack('V', $payload);
        if (!isset($value[1])) {
            throw new ReaderException(
                sprintf('Cannot resolve value at offset %d', $start),
                1539614261
            );
        }
        return $value[1];
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
