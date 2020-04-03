# BotDaddy
Telegram bot with many functions

Создание диалога/монолога из нескольких сообщений:
пример:
/fwd_to_text
George: Hi (message 0)
Julia: Hi (message 1)
/stop
result:
  xxx: Hi (message 2)
  yyy: Hi (message 2)

in settings you may customize if the result should be anonimous (xyz...) or public (not xyz, but names) and create your own dictionaries instead xyz...

Предупреждение: может не работать правильно с фловардами от пользователей со скрытыми форвардами в режиме диалога (только если их несколько в диалоге, и у них идентичные ники)


Pins:
 /pin - Пин
 /pin 1 - пин без уведомления
 /pintime - Несколько пинов подряд, по умолчанию 3, чтобы задать количество, нужно написать число после команды
 /pinlist - Список всех пинов(сделанными живыми людьми, не ботами!!) после добавления бота

Bans:
 /ban - Бан участника чата
 /unban - Анбан участника чата
  Также в конфиге настраиваются списки текстовых сообщений для бана и анбана

Mutes:
 !мут - Мут участника чата
 !анмут - Анмут участника чата
!!!Регистр не учитывается!!!

Other commands and functions:
 /chat_id - Выводит id чата
 /user - твои айди, юзернейм и имя
 /user (replay) - айди отправителя, его юзернейм и имя
 /user <id> - айди, юзернейм и имя владельца id
 /ke - Проверка бота
 /time <local or UTC-format> - время в местности (примеры: /time Moscow, /time Russia (не стоит вообще, сами понимаете почему, надеюсь кек), /time Санкт-Петербург, Богатырский проспект), или в часовом поясе (примеры: /time UTC, /time UTC+1). Использует LocationIQ и TimeZoneFinder.
 /weather <local> - погода в местности(примеры, как в /time). Использует LocationIQ и OpenWeatherMap.
 /gramota <word> - показывает инфо о слове с сайта gramota.ru
 /mask <msk> - подбирает слова по маске (пример: <user> /mask маска; <bot> маска, масса, масия, масла)
 /spell - проверят текст на орфографические ошибки. Можно использовать реплаем на текст или текстом после команды. Использует Yandex Speller.
 /get_first_msg (reply) - получить первое сообщение юзера в чате. (Если чат приватный, то в чате также должен присутствовать @P1voknopka); не работает с удаленными аккаунтами, и если @P1voknopka недоступно нужное сообщение (такое возможно в приватных чатах с историей, закрытой для новых участников)
 /get_message (reply) - инфа о сообщении в реплае, если без реплая, то сообщения с командой
 /q (reply) - получить цитату-стикер сообщения, если без реплая, то сообщения с командой
 /create_list (reply) - создать список
 /help - Выводит это сообщение
 /help <command> - Выводит справку по команде
 /help_define - Обновляет это сообщение, только для разработчиков бота

HangBot_helper:
 /run_changer - чистка флуда после игры в [hangbot](t.me/hangbot), очищает все сообщения игры с hangbot-ом с момента последнего запуска на хосте, если реплай к hangbot-у, то удаляет сообщение, на которое сделан реплай, если оно - последнее в игре, то бот отправляет результат этой игры в сокращенном варианте. Если во время игры были иногда слишком часто буквы названы, чаще, чем HangBot отвечал, то некоторые сообщения не будут удалены, это вам не юзербот😔. И показывает стату* (если не отключена) с последней чистки(или с перезапуска бота) до этой.
 /hangstats_switch - переключает автопоказ статы* после чистки
 /winrate <reply> - отправьте в ответ к сообщению статы(не топа!) от hangbot-a и получите винрейт
* - стата не хэнгбота, а от процесса игры, собираемая BotDaddy, ну она по умолчанию включена, так что если играете, то увидите!
