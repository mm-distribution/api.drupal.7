# LocaleImportFunctionalTest::getPoFileWithMsgstr()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1291–1308 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1291-L1308)
- **Class:** [LocaleImportFunctionalTest](../LocaleImportFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function getPoFileWithMsgstr()
```

## Documentation

```text
Helper function that returns a .po file with an empty last item.
```

## Code

```php
  function getPoFileWithMsgstr() {
    return <<< EOF
msgid ""
msgstr ""
"Project-Id-Version: Drupal 7\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n > 1);\\n"

msgid "Operations"
msgstr "Műveletek"

msgid "Will not appear in Drupal core, so we can ensure the test passes"
msgstr ""

EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
