# Reader

- **Type:** Class
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Reader.php`](_file.md), lines 14–254 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php#L14-L254)

## Signature

```php
class Reader
```

## Documentation

_No docblock in source._

## Properties

### $fileName

```php
private $fileName;
```

```text
@var string
```

### $fileType

```php
private $fileType;
```

```text
Mime-type in order to use zlib, bzip2 or no compression.
In case ext-fileinfo is not present only the relevant types
'application/x-gzip' and 'application/x-bzip2' are assigned
to this class property.

@var string
```

## Methods (derived index)

- [__construct()](Reader/__construct.md)
- [resolveContainer()](Reader/resolveContainer.md)
- [extractData()](Reader/extractData.md)
- [resolveStream()](Reader/resolveStream.md) — Resolves stream in order to handle compressed Phar archives.
- [determineFileType()](Reader/determineFileType.md)
- [determineFileTypeByHeader()](Reader/determineFileTypeByHeader.md) — In case ext-fileinfo is not present only the relevant types 'application/x-gzip' and 'application/x-bzip2' are resolved.
- [resolveManifestLength()](Reader/resolveManifestLength.md)
- [resolveFourByteLittleEndian()](Reader/resolveFourByteLittleEndian.md)
- [resolveTwoByteBigEndian()](Reader/resolveTwoByteBigEndian.md)

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Reader.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Reader.php) · Licensed GPL-2.0-or-later (see LICENSE)._
