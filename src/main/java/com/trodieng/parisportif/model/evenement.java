package com.trodieng.parisportif.model;

import java.time.*;

import javax.persistence.*;

import org.openxava.model.*;

import lombok.*;
@Entity @Getter @Setter
public class evenement extends Identifiable  {
	private String label;
	private float cote;
    private String score;
    private LocalDate date;

}
