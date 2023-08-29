class BaseEvent(object):
    def __init__(self, fields, event_name="Event", key_fields=(), recguid=None):
        self.recguid = recguid
        self.name = event_name
        self.fields = list(fields)
        self.field2content = {f: None for f in fields}
        self.nonempty_count = 0
        self.nonempty_ratio = self.nonempty_count / len(self.fields)

        self.key_fields = set(key_fields)
        for key_field in self.key_fields:
            assert key_field in self.field2content

    def __repr__(self):
        event_str = "\n{}[\n".format(self.name)
        event_str += "  {}={}\n".format("recguid", self.recguid)
        event_str += "  {}={}\n".format("nonempty_count", self.nonempty_count)
        event_str += "  {}={:.3f}\n".format("nonempty_ratio", self.nonempty_ratio)
        event_str += "] (\n"
        for field in self.fields:
            if field in self.key_fields:
                key_str = " (key)"
            else:
                key_str = ""
            event_str += (
                "  "
                + field
                + "="
                + str(self.field2content[field])
                + ", {}\n".format(key_str)
            )
        event_str += ")\n"
        return event_str

    def update_by_dict(self, field2text, recguid=None):
        self.nonempty_count = 0
        self.recguid = recguid

        for field in self.fields:
            if field in field2text and field2text[field] is not None:
                self.nonempty_count += 1
                self.field2content[field] = field2text[field]
            else:
                self.field2content[field] = None

        self.nonempty_ratio = self.nonempty_count / len(self.fields)

    def field_to_dict(self):
        return dict(self.field2content)

    def set_key_fields(self, key_fields):
        self.key_fields = set(key_fields)

    def is_key_complete(self):
        for key_field in self.key_fields:
            if self.field2content[key_field] is None:
                return False

        return True

    def get_argument_tuple(self):
        args_tuple = tuple(self.field2content[field] for field in self.fields)
        return args_tuple

    def is_good_candidate(self, min_match_count=2):
        key_flag = self.is_key_complete()
        if key_flag:
            if self.nonempty_count >= min_match_count:
                return True
        return False


class DefendantEvent(BaseEvent):
    # 姓名、性别、民族、出生年月日、户籍地、#出生地、住所地
    # 逮捕时间、起诉时间
    NAME = "Defendant"
    FIELDS = [
        "DefendantName",
        "DefendantSex",
        "DefendantNation",
        "DefendantBirth",
        "Hujidi",
        #'ArrestTime',
        #'ProsecutionTime'
        "Control",  # 是否管制
        "ControlTime",
        "Detention",  # 是否拘役
        "DetentionTime",
        "Imprisonment",  # 是否有期徒刑
        "ImprisonmentTime",
        "PoliticalRights",  # 是否剥夺政治权利
        "PoliticalRightsTime",
        "Fine",  # 是否判处罚金
        "FineNum",
        "PartofProperty",  # 是否没收部分财产
        "PartofPropertyNum",
        "AllProperty",  # 是否没收全部财产
        "AllPropertyNum",
        "EcoCompensation",  # 是否需要赔偿经济损失
        "EcoCompensationNum",
        "VictimName"
    ]

    TRIGGERS = {
        1: ["DefendantName"],
        2: ["DefendantName", "DefendantSex"],
        3: ["DefendantName", "DefendantSex", "VictimName"],
        4: ["DefendantName", "DefendantSex", "DefendantNation", "VictimName"],
        5: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "VictimName",
        ],
        6: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "VictimName",
        ],
        7: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "VictimName",
        ],
        8: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "VictimName",
        ],
        9: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "VictimName",
        ],
        10: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "VictimName",
        ],
        11: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "VictimName",
        ],
        12: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "VictimName",
        ],
        13: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "VictimName",
        ],
        14: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "VictimName",
        ],
        15: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "Fine",
            "VictimName",
        ],
        16: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "Fine",
            "FineNum",
            "VictimName",
        ],
        17: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "Fine",
            "FineNum",
            "PartofProperty",
            "VictimName",
        ],
        18: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "Fine",
            "FineNum",
            "PartofProperty",
            "PartofPropertyNum",
            "VictimName",
        ],
        19: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "Fine",
            "FineNum",
            "PartofProperty",
            "PartofPropertyNum",
            "AllProperty",
            "VictimName",
        ],
        20: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "Fine",
            "FineNum",
            "PartofProperty",
            "PartofPropertyNum",
            "AllProperty",
            "AllPropertyNum",
            "VictimName",
        ],
        21: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "Fine",
            "FineNum",
            "PartofProperty",
            "PartofPropertyNum",
            "AllProperty",
            "AllPropertyNum",
            "EcoCompensation",
            "VictimName",
        ],
        22: [
            "DefendantName",
            "DefendantSex",
            "DefendantNation",
            "DefendantBirth",
            "Hujidi",
            "Control",
            "ControlTime",
            "Detention",
            "DetentionTime",
            "Imprisonment",
            "ImprisonmentTime",
            "PoliticalRights",
            "PoliticalRightsTime",
            "Fine",
            "FineNum",
            "PartofProperty",
            "PartofPropertyNum",
            "AllProperty",
            "AllPropertyNum",
            "EcoCompensation",
            "EcoCompensationNum",
            "VictimName"
        ],
    }

    TRIGGERS[
        "all"
    ] = "['DefendantName', 'DefendantSex', 'DefendantNation', 'DefendantBirth', 'Hujidi', 'Control', 'ControlTime', 'Detention', 'DetentionTime', 'Imprisonment', 'ImprisonmentTime', 'PoliticalRights', 'PoliticalRightsTime', 'Fine', 'FineNum', 'PartofProperty', 'PartofPropertyNum', 'AllProperty', 'AllPropertyNum', 'EcoCompensation', 'EcoCompensationNum','VictimName']"

    def __init__(self, recguid=None):
        super().__init__(self.FIELDS, event_name=self.NAME, recguid=recguid)
        self.set_key_fields(self.TRIGGERS)


class VictimEvent(BaseEvent):
    NAME = "Victim"
    FIELDS = [
        "VictimName",
        "VictimAge",
        "VictimBirth",
        "VictimSex",
        "DieorNot",
        "Victim2Defendant",
    ]
    TRIGGERS = {
        1: ["VictimName"],
        2: ["VictimName", "VictimAge"],
        3: ["VictimName", "VictimAge", "VictimBirth"],
        4: ["VictimName", "VictimAge", "VictimBirth", "VictimSex"],
        5: ["VictimName", "VictimAge", "VictimBirth", "VictimSex", "DieorNot"],
        6: [
            "VictimName",
            "VictimAge",
            "VictimBirth",
            "VictimSex",
            "DieorNot",
            "Victim2Defendant",
        ],
    }

    TRIGGERS[
        "all"
    ] = "['VictimName', 'VictimAge', 'VictimBirth', 'VictimSex', 'DieorNot', 'Victim2Defendant']"

    def __init__(self, recguid=None):
        super().__init__(self.FIELDS, event_name=self.NAME, recguid=recguid)
        self.set_key_fields(self.TRIGGERS)


class CaseEvent(BaseEvent):
    NAME = "Case"
    FIELDS = [
        "CaseNumber",
        "Committee",  # 是否提交审判委员会讨论
        "PrivateProsecution",  # *是否自诉案件
    ]

    TRIGGERS = {
        1: ["CaseNumber"],
        2: ["CaseNumber", "Committee"],
        3: ["CaseNumber", "Committee", "PrivateProsecution"],
    }

    TRIGGERS["all"] = "['CaseNumber', 'Committee', 'PrivateProsecution']"

    def __init__(self, recguid=None):
        super().__init__(self.FIELDS, event_name=self.NAME, recguid=recguid)
        self.set_key_fields(self.TRIGGERS)


common_fields = ["CaseNumber"]

event_type2event_class = {
    DefendantEvent.NAME: DefendantEvent,
    # VictimEvent.NAME: VictimEvent,
    # CaseEvent.NAME: CaseEvent,
}

event_type_fields_list = [
    (DefendantEvent.NAME, DefendantEvent.FIELDS,DefendantEvent.TRIGGERS,2),
    # (VictimEvent.NAME, VictimEvent.FIELDS,VictimEvent.TRIGGERS,2),
    # (CaseEvent.NAME, CaseEvent.FIELDS,CaseEvent.TRIGGERS,2),
]
