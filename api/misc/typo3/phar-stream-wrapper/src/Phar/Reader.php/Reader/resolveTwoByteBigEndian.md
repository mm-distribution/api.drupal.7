# Reader::resolveTwoByteBigEndian()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](../_file.md), lines 235–253 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L235-L253)
- **Class:** [Reader](../Reader.md)

## Signature

```php
public static function resolveTwoByteBigEndian($content, $start)
```

## Documentation

```text
@param string $content
@param int $start
@return int
```

## Code

```php
    public static function resolveTwoByteBigEndian($content, $start)
    {
        $payload = substr($content, $start, 2);
        if (!is_string($payload)) {
            throw new ReaderException(
                sprintf('Cannot resolve value at offset %d', $start),
                1539614263
            );
        }

        $value = unpack('n', $payload);
        if (!isset($value[1])) {
            throw new ReaderException(
                sprintf('Cannot resolve value at offset %d', $start),
                1539614264
            );
        }
        return $value[1];
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
