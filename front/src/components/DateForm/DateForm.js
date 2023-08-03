//компонент выбора даты, принимает стор от которого инициализируется, методы оnСhange 
import React, { useEffect } from "react"
import { observer } from "mobx-react-lite"


import dayjs from 'dayjs';
import { Form, DatePicker } from "antd"
export const DateForm = observer((props) => {
    const dateFormat = 'DD.MM.YYYY';
    useEffect(() => {
        console.log("useEffect DateForm", props)
        if (props.store.period.length === 0) {
            console.log(" пустой setPeriod today ")
            props.store.setPeriod([dayjs().format(dateFormat), dayjs().format(dateFormat)])   
        }
        else {
            console.log("не пустой период ")
        }
    }, [])

   
    const rangePresets = [
        {
            label: 'Сегодня',
            value: [dayjs().add(0, 'd'), dayjs()],
        },
        {
            label: 'Вчера',
            value: [dayjs().add(-1, 'd'), dayjs()],
        },
        {
            label: 'Неделя',
            value: [dayjs().add(-7, 'd'), dayjs()],
        },
        {
            label: 'Месяц',
            value: [dayjs().add(-30, 'd'), dayjs()],
        },
    ];

    return (

        <div>
            <Form
                layout="inline"
                style={{ rowGap: "5px", marginBottom: "2px" }}
            >
                <Form.Item
                    name="dates"
                    initialValue={
                        props.store.period.length?
                            props.store.period.map((item) => (dayjs(item,dateFormat))) :
                            [dayjs(), dayjs()]
                    }
                >
                    <DatePicker.RangePicker
                        onChange={props.onChange}
                        presets={rangePresets}
                        format={"DD.MM.YYYY"}
                    />
                </Form.Item>
            </Form>
        </div>
    )
})