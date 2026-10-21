# Manifest::fromContent()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php`](../_file.md), lines 23–42 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php#L23-L42)
- **Class:** [Manifest](../Manifest.md)

## Signature

```php
public static function fromContent($content)
```

## Documentation

```text
@param string $content
@return self
@see http://php.net/manual/en/phar.fileformat.phar.php
```

## Code

```php
    public static function fromContent($content)
    {
        $target = new static();
        $target->manifestLength = Reader::resolveFourByteLittleEndian($content, 0);
        $target->amountOfFiles = Reader::resolveFourByteLittleEndian($content, 4);
        $target->flags = Reader::resolveFourByteLittleEndian($content, 10);
        $target->aliasLength = Reader::resolveFourByteLittleEndian($content, 14);
        $target->alias = substr($content, 18, $target->aliasLength);
        $target->metaDataLength = Reader::resolveFourByteLittleEndian($content, 18 + $target->aliasLength);
        $target->metaData = substr($content, 22 + $target->aliasLength, $target->metaDataLength);

        $apiVersionNibbles = Reader::resolveTwoByteBigEndian($content, 8);
        $target->apiVersion = implode('.', array(
            ($apiVersionNibbles & 0xf000) >> 12,
            ($apiVersionNibbles & 0x0f00) >> 8,
            ($apiVersionNibbles & 0x00f0) >> 4,
        ));

        return $target;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Manifest.php) · Licensed GPL-2.0-or-later (see LICENSE)._
